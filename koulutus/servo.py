from microbit import *
import radio

# Servo
MIN_VAL = 0.02*1023
MAX_VAL = 0.12*1023

# Motor
#MIN_VOLTAGE = 0.0
#MAX_VOLTAGE = 1.0

pin0.set_analog_period(20) # Valmistellaan pin0 servoa varten (asetetaan PWM periodi 20 millisekuntiin)

radio.on() # Radio paalle
radio.config(channel = 50) # Valitse kanava 0-100 valilta

while True: # Toistetaan ikuisesti

    viesti = radio.receive() # Etsitaan ilmasta viesti

    if viesti != None: # Viesti loytyi!
        potentiometri = int(viesti) # Muutetaan viesti luvuksi
        dc = int((MAX_VAL - MIN_VAL)/1023.0*potentiometri + MIN_VAL)
        #dc = potentiometri * (MAX_VOLTAGE - MIN_VOLTAGE) + MIN_VOLTAGE # Muokataan potentiometrin arvo sopivaksi (2% ja 12% valille)
        pin0.write_analog(dc) # Liikutetaan servoa

    sleep(10) # Nukutaan 10 millisekuntia jottei toistolause mene liian nopeasti
