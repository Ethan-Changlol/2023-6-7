# Imports go at the top
from microbit import *
import neopixel
np=neopixel.NeoPixel(pin12,8)



np[2]=(255,255,255)
np[1]=(255,255,255)
np[5]=(255,0,0)
np[6]=(255,0,0)
np.show()
def right_on():
    np[0]=(255,100,0)
    np[7]=(255,100,0)
    np.show()
def right_off():
    np[0]=(0,0,0)
    np[7]=(0,0,0)
    np.show()
def left_on():
    np[3]=(255,100,0)
    np[4]=(255,100,0)
    np.show()
def left_off():
    np[3]=(0,0,0)
    np[4]=(0,0,0)
    np.show()
