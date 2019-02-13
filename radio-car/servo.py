from microbit import *
import radio

MIN_VOLTAGE = 0.0
MAX_VOLTAGE = 1.0

PIN_MOTOR_R = pin1;
PIN_MOTOR_L = pin0;

suunta = 0
kaasu = 0

PIN_MOTOR_R.set_analog_period_microseconds(200)
PIN_MOTOR_L.set_analog_period_microseconds(200)

radio.on() # Radio päälle
radio.config(channel = 50) # Valitse kanava 0-100 väliltä

def to_voltage(val):
    return max(MIN_VOLTAGE, min(MAX_VOLTAGE, val * (MAX_VOLTAGE - MIN_VOLTAGE) + MIN_VOLTAGE))
#This is a comment.
while True: # Toistetaan ikuisesti
    viesti = radio.receive() # Etsitään ilmasta viesti

    if viesti != None: # Viesti löytyi!
        split = viesti.split(":")
        if split[0] == "k":
            kaasu = float(viesti[1]) / 1024.0 # 0..1
        if split[0] == "s":
            suunta = float(viesti[1]) / 1024.0 - 0.5 # -0.5..0.5
        PIN_MOTOR_L.write_analog(to_voltage(kaasu * min(1, 1 + suunta)))
        PIN_MOTOR_R.write_analog(to_voltage(kaasu * min(1, 1 - suunta)))
