import network
import socket
from utime import sleep
from machine import ADC, Pin
from time import ticks_ms, ticks_add, ticks_diff


#analog_value = machine.ADC(26)
#conversion_factor = 3.3/(1<<12)
ADC_PIN = Pin(26, mode=Pin.IN) # The microphone AUD is connected to pin 26 on the pico
MIC = ADC(ADC_PIN) # The pin on which to read from the ADC
VREF = 3.3 # The supply voltage, which affects for the readings from the ADC
RANGES = 1 << 16 # Because of the 12-bit ADC of the pico being upsampled to 16 in micropython. This is equal to 65536
MAX_RES = 65536
CONV = VREF / RANGES # The resolution of the ADC is roughly 0.8 millivolts


samples = []

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


def ptp_to_volts(ptp_amp):
    """Turn the peak to peak amplitude into volts"""
    
    amplitude_as_volts = (ptp_amp * VREF) / MAX_RES
    
    return amplitude_as_volts

def value_mapping(volt_reading):
    """ Map the volts onto a scale from 1 to 10"""
    
    normalized_volts = volt_reading / VREF
    mapped_value = normalized_volts * 10
    rounded_value = round(mapped_value, 2) # Round value to only two decimals
    
    return rounded_value

x = 0
while x < 500:
    ptp_amp = ptp()
    volts = ptp_to_volts(ptp_amp)
    final_value = value_mapping(volts)
    print(final_value)
    x += 1
    

#try:
#    connect()
#except KeyboardInterrupt:
#    machine.reset()
    
def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect('Betania', '1234567890!')
    
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
        ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip
