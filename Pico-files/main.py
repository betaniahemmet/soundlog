import network
import urequests
from secret import ssid, password
from machine import ADC, Pin, unique_id
from time import ticks_ms, ticks_add, ticks_diff, time, sleep
from ubinascii import hexlify

"""
This is the firmware for a raspberry pi pico w that is supposed
to collect the sound amplitude in the surrounding and send it
with a timestamp to be stored in a database.
"""


ADC_PIN = Pin(26, mode=Pin.IN)  # The microphone AUD is connected to pin 26 on the pico
MIC = ADC(ADC_PIN)  # The pin on which to read from the ADC
VREF = 3.3  # The supply voltage, which affects for the readings from the ADC
RANGES = (
    1 << 16
)  # Because of the 12-bit ADC of the pico being upsampled to 16 in micropython. This is equal to 65536
MAX_RES = 65536  # As stated above. Will use this instead
CONV = VREF / MAX_RES  # The resolution of the ADC is roughly 0.8 millivolts
PICO_ID = hexlify(unique_id()).decode() # The unique id of the pico
max_amplitude = None


def ptp():
    """A function to find the peak to peak amplitude of the raw signal"""
    max_amp = 0
    min_amp = 65536
    deadline = ticks_add(ticks_ms(), 50)
    while ticks_diff(deadline, ticks_ms()) > 0:
        adc_raw = MIC.read_u16()
        if adc_raw < MAX_RES:
            if adc_raw > max_amp:
                max_amp = adc_raw
            elif adc_raw < min_amp:
                min_amp = adc_raw

    ptp_amp = max_amp - min_amp

    return ptp_amp


def ptp_to_volts(ptp_amp):
    """Convert the peak-to-peak amplitude into volts"""

    amplitude_as_volts = (
        ptp_amp * CONV
    )  # Apply the conversion factor to the meassurement

    return amplitude_as_volts


def value_mapping(volt_reading):
    """Map the volts onto a scale from 1 to 10"""

    normalized_volts = volt_reading / VREF
    mapped_value = normalized_volts * 10
    rounded_value = round(mapped_value, 2)  # Round value to only two decimals
    formatted_value = float(
        "{:.2f}".format(rounded_value)
    )  # Compensating for fringe cases
    return formatted_value


def connect():
    """Connect to WLAN"""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.disconnect()

    try:
        wlan.connect(ssid, password)

        while not wlan.isconnected():
            print("Waiting for connection...")
            sleep(2)
        
        message = f"Connected on {wlan.ifconfig()[0]}"
        write_to_log_file(message)
        print(message)

        return wlan.ifconfig()[0]

    except Exception as e:
        error_message(f"Failed to connect to {ssid}: {e}")
        write_to_log_file(error_message)
        
        return wlan.status()
    
def write_to_log_file(message):
    """
    Write the provided message to a custom log file.
    """
    log_file = "log.txt"

    with open(log_file, "a") as file:
        file.write(f"{message}\n")


def send_measurement(value):
    """
    Send measurement to the remote server
    """
    ip = "192.168.1.239:5000"

    url = f"http://{ip}/measurements"
    data = {"pico_id": PICO_ID,
            "value": value,
            "timestamp" : time()}

    try:
        response = urequests.post(url, json=data)
        response.close()

    except Exception as e:
        error_message("Error sending measurement: %s", e)
        write_to_log_file(error_message)

connection = connect()
last_sent_time = time()

print("Measurement collection started...")  # Print statement indicating that measurement collection has started

while True:
    try:
        ptp_amp = ptp()  # Get peak to peak value
        volts = ptp_to_volts(ptp_amp)  # Convert to volts
        final_value = value_mapping(volts)  # Map to number between 0 and 10
        if max_amplitude is None or final_value > max_amplitude:
            max_amplitude = final_value  # Update max value
        
        if time() - last_sent_time >= 5:  # Wait five seconds
            send_measurement(max_amplitude)  # Send max value
            max_amplitude = None
            last_sent_time = time()  # Wipe the timer

    except Exception as e:
        error_message = f"An error occurred in the while loop: {e}"
        write_to_log_file(error_message)
