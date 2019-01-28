from microbit import *
from neopixel import NeoPixel
import radio
 
num_pixels = 24
foreground = [0, 0, 255]  # rgb color for led - red, green and blue
background = [10, 10, 10]
background_off = [0, 0, 0]

ledCount = 1
prevLedCount = 0

ring = NeoPixel(pin0, num_pixels)


for i in range (0, num_pixels):
    ring[i] = background
    ring.show()
    sleep(50)
radio.on() # Radio paalle
radio.config(channel = 50) # Valitse kanava 0-100 valilta
sleep(2000)

while True:

    if button_a.is_pressed():
        ledCount = ledCount +1
        if ledCount > num_pixels:
            ledCount = 1
    if button_b.is_pressed():
        ledCount = ledCount -1
        if ledCount < 1:
            ledCount = num_pixels

    if ledCount != prevLedCount:
        for i in range (0, num_pixels):
            ring[i] = background_off
            ring.show()
            sleep(10)
    
        for i in range (0, ledCount):
            ring[i] = foreground
            ring.show()
            sleep(10)

    prevLedCount = ledCount
    viesti = radio.receive() # Etsitaan ilmasta viesti

    if viesti != None:
        arvo = int(viesti)
        numLeds = int(arvo*num_pixels/1023.0)
    
        #sammutetaan ledit
        for i in range (0, num_pixels):
            ring[i] = background_off
            ring.show()
        
        for i in range(0, numLeds):
            ring[i] = foreground     # set pixel i to foreground
            ring.show()              # actually display it
            

    sleep(30)