from microbit import *
from neopixel import NeoPixel
import radio

# LED-renkaan tai -nauhan pituus
PIXELS = 24

# Pelin varit RGB-arvoina
TARGET_COLOR = [0,16,0]
OBJECT_COLOR = [64,0,0]
BOTH_COLOR = [128,128,0]

# Suurempi INITIAL_SPEED on hitaampi
INITIAL_SPEED = 100
# Vaikuttaa siihen, kuinka nopeasti peli kiihtyy
FACTOR = 0.9

# Maaritetaan targetin rajat
LOWER_LIMIT = 11
UPPER_LIMIT = 13

ring = NeoPixel(pin0, PIXELS)

def game():
    # Aloitetaan uusi peli. Asetetaan pelin muuttujat alkuarvoihinsa
    score = 0
    position = 0
    alive = True
    speed = INITIAL_SPEED

    # Nollataan painikkeen laskuri
    button_a.get_presses()
    # Piirretaan naytolle pistemaara
    display.show(score)
    # Piirretaan NeoPixeleihin tyhja pelialue ja target
    for i in range(0, PIXELS):
        if is_target(i):
            ring[i] = TARGET_COLOR
        else:
            ring[i] = [0,0,0]

    # Jatketaan pelin suorittamista niin pitkaan, kuin pelaaja on elossa
    while alive:
        # Liikutetaan objectia pelialueella move-funktiolla ja asetetaan
        # uusi sijainti position-muuttujan arvoksi
        position = move(position, PIXELS)
        # Tulostetaan paivittynyt pelitilanne NeoPixeleille
        ring.show()
        # Annetaan pelaajalle reaktioaikaa
        sleep(speed)

        # Tarkistetaan, painettiinko nappia nykyisen pisteen kohdalla
        if button_a.get_presses() > 0:
            # Jos nappia painettiin targetin paalla, lisataan piste ja nopeutetaan pelia
            if is_target(position):
                score += 1
                speed =  int(speed * FACTOR)
                # Tulostetaan pistemaaran viimeinen numero naytolle
                display.show(str(score % 10))
            else:
                alive = False

    # Nollataan painikkeen laskuri
    button_b.get_presses()

    # Naytetaan surunaamaa sekunnin ajan
    display.show(Image.SAD)
    sleep(1000)

    # Naytetaan pelaajan pistemaaraa kunnes painiketta painetaan
    while button_b.get_presses() == 0:
        display.scroll(str(score))




def move(current, loop_length):
    # Jos vanha sijainti on targetin rajojen sisalla
    if is_target(current):
        # Sijainti on targetin varinen
        ring[current] = TARGET_COLOR
    else:
        # Sijainti on tyhja
        ring[current] = [0,0,0]

    # Uusi sijainti on vanhan sijainti + 1, paitsi pelialueen ulkopuolelle
    # mentaessa palataan pelialueen alkuun modulolla
    new = (current + 1) % PIXELS

    # Jos uusi sijainti on targetin rajojen sisalla
    if is_target(new):
        # Sijainti on seka targetin etta objectin varinen
        ring[new] = BOTH_COLOR
    else:
        # Sijainti on objectin varinen
        ring[new] = OBJECT_COLOR

    # Palautetaan uuden sijainnin arvo
    return new

# Tarkistaa, onko sijainti targetin sisalla ja palauttaa True tai False
def is_target(value):
    return LOWER_LIMIT <= value <= UPPER_LIMIT

# Ajetaan pelin paafunktiota ikuisesti
while True:
    game()
