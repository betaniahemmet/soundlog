import network
import socket
from secret import ssid, password
from machine import ADC, Pin
from time import ticks_ms, ticks_add, ticks_diff, sleep


#analog_value = machine.ADC(26)
#conversion_factor = 3.3/(1<<12)
ADC_PIN = Pin(26, mode=Pin.IN) # The microphone AUD is connected to pin 26 on the pico
MIC = ADC(ADC_PIN) # The pin on which to read from the ADC
VREF = 3.3 # The supply voltage, which affects for the readings from the ADC
RANGES = 1 << 16 # Because of the 12-bit ADC of the pico being upsampled to 16 in micropython. This is equal to 65536
MAX_RES = 65536
CONV = VREF / RANGES # The resolution of the ADC is roughly 0.8 millivolts


def ptp():
    """A function to find the peak to peak amplitude of the raw signal"""
    max_amp = 0
    min_amp = 65536
    adc_raw = MIC.read_u16()
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
    # TODO: Maybe take several readings and send back the max-value to get a more acurate estimation of the actual noise situation


def ptp_to_volts(ptp_amp):
    """Turn the peak to peak amplitude into volts"""
    
    amplitude_as_volts = (ptp_amp * VREF) / MAX_RES
    
    return amplitude_as_volts

def value_mapping(volt_reading):
    """ Map the volts onto a scale from 1 to 10"""
    
    normalized_volts = volt_reading / VREF
    mapped_value = normalized_volts * 10
    rounded_value = round(mapped_value, 2) # Round value to only two decimals
    formatted_value = float("{:.2f}".format(rounded_value))
    return formatted_value

    
def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(2)
        ip = wlan.ifconfig()[0]
    return ip


def open_socket():
    # Open socket
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    
    return addr, s
    
def listen(final_value, addr, s):
    

    cl, addr = s.accept()
    print('client connected from', addr)
    request = cl.recv(1024)
    print(request)
    # Do not unpack request
    # We reply to any request the same way


    
    response = str(final_value) # This is what we send in reply

    cl.send(response)
    print("Sent:" + response)
    cl.close()




fresh_ip = connect()
print(f'Connected on {fresh_ip}')


addr, s = open_socket()
print(addr, s)

counter = 0 
max_value = 0
    
while True:
    try:
        ptp_amp = ptp()
        volts = ptp_to_volts(ptp_amp)
        final_value = value_mapping(volts)
        
        listen(final_value, addr, s)

    
    
    
    except OSError as e:
        cl.close()
        print('connection closed')
    
    except KeyboardInterrupt:
        print("Resetting machine")
        machine.reset()
        




