import network
import socket
from utime import sleep
from machine import ADC, Pin


#analog_value = machine.ADC(26)
#conversion_factor = 3.3/(1<<12)
ADC_PIN = Pin(26, mode=Pin.IN)
MIC = ADC(ADC_PIN) # The port on which to read from the ADC
VREF = 3.3 # The supply voltage, which affects for the readings from the ADC
RANGES = 1 << 16 # Because of the 16-bit ADC of the pico. This is equal to 65536
MAX_RES = 65536
CONV = VREF / RANGES # The resolution of the ADC is roughly 0.8 millivolts

samples = []


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

while True:
    adc_raw = MIC.read_u16()
    sample = round(adc_raw * CONV, 2)
    samples.append(sample)
    # sleep(0.001)
    if len(samples) == 1000:
        print(max(samples))
        samples = []
        
#try:
#    connect()
#except KeyboardInterrupt:
#    machine.reset()
    

