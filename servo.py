from microbit import *

# Kun kutsutaan write_angle, piirretaanko kulma myos LED-naytolle?
# (Testaamista varten kannattaa olla True.)
DRAW_ANGLE_ON_LEDS = True

def main():
    # Tama ohjelma pyorittaa servoa edes takaisin. Pieni servodemo.
    write_angle(0)
    sleep(500)
    write_angle(90)
    sleep(500)
    write_angle(45)
    sleep(500)
    write_angle(90)
    sleep(500)
    write_angle(135)
    sleep(500)
    write_angle(90)
    sleep(500)
    write_angle(180)

# Servon ohjausfunktiot
# Pin micro:bitissa johon servo pistetaan kiinni
SERVO_PIN = pin0
# Servon mahdollinen pyorimiskulma
SERVO_ANGLE = 180
# Servon maksimi signaalin pituus
SERVO_MAX_MCS = 2400
# Servon minimi signaalin pituus
SERVO_MIN_MCS = 600
# Servon signaalin taajuus
SERVO_FREQ = 50
def write_microseconds(mcs):
    mcs = min(SERVO_MAX_MCS, max(SERVO_MIN_MCS, mcs))
    duty = round(mcs * 1024 * SERVO_FREQ // 1000000)
    SERVO_PIN.write_analog(duty) # Turn the servo
    SERVO_PIN.write_digital(0)   # Se the pin off

# Tata kutsumalla on tarkoitus ohjata servoa, ylla on tekninen puoli
def write_angle(degrees):
    degrees = degrees % 360

    if DRAW_ANGLE_ON_LEDS:
        clock = ((degrees + 270) // 30) % 12
        display.show(Image.ALL_CLOCKS[clock])

    total_range = SERVO_MAX_MCS - SERVO_MIN_MCS
    mcs = SERVO_MIN_MCS + total_range * degrees // SERVO_ANGLE
    write_microseconds(mcs)

# Kutsutaan main, aloittaa ohjelman
main()
