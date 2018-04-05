'''
Analog output pwm -ohjauksella. Katso: https://en.wikipedia.org/wiki/Pulse-width_modulation
'''
from microbit import *

pin0.set_analog_period(20)  # Asetetaan jaksonaika 20 ms. jaksonaika = 1/ taajuus

while True:
    for pulssisuhde in range(0, 101, 5):  # kasvatetaan pulssisuhdetta 0% aina 100%:iin 5%:n lisayksella.
        pin0.write_analog(pulssisuhde)
        sleep(50)
    sleep(2000)
    for pulssisuhde in range(100, -1, -5):
        pin0.write_analog(pulssisuhde)
        sleep(50)
        
    sleep(2000)