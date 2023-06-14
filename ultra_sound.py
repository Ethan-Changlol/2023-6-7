# Imports go at the top
from microbit import *
import machine


display.off()

def distance():
    # trigger ultra sound wave
    pin3.write_digital(1)
    pin3.write_digital(0)
    micros=machine.time_pulse_us(pin9,1)
    v= 340*100/1000000
    d=micros/2*v
    return d



while True:
    print(distance())
    sleep(1000)
