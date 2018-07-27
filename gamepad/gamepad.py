from microbit import *

# Maaritellaan pinnit
NAPPI = pin8
JOYSTICK_X = pin2
JOYSTICK_Y = pin1
JOYSTICK_THUMB = pin0

while True:
    # Luetaan data
    nappi = NAPPI.read_digital()
    joystick_x = JOYSTICK_X.read_analog()
    joystick_y = JOYSTICK_X.read_analog()
    joystick_thumb = JOYSTICK_THUMB.read_digital()

    # Koodataan data
    data = "{},{},{},{}".format(nappi, joystick_x, joystick_y, joystick_thumb)

    # Kirjoitetaan data sarjaliikenteeseen
    # oletuksena symbolinoupeutena on 115200
    print(data)

    # Nukutaan tarpeeksi, etta datan lukija pysyy mukana
    sleep(15) #ms
