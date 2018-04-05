from microbit import *
import math

# Pinit
PIN_ECHO = pin0
PIN_TRIG = pin1

# Minimietaisyys joka nakyy naytolla
MIN_DIST = 5.0
# Etaisyys joka mahtuu naytolle (nakyva alue on siis MIN_DIST..MIN_DIST+DIST)
DIST = 30.0


# Toistofunktio (tassa tapahtuvat asiat tapahtuvat 50 kertaa sekunnissa jatkuvasti)
# (kts. tiedoston viimeiset rivit kutsua varten)
def loop():
    # Kaynnistetaan sensori
    trigger_echo()
    # Mitataan kaiun kesto
    duration = poll_duration()
    # Lasketaan matka
    distance = duration_to_distance(duration)
    # Esitetaan matka LED-ruudulla
    show_distance(distance)
    display.set_pixel(0,0,9)
    #display.scroll("D: " + str(distance))


# Kaynnista kaiku (mittaamista varten)
def trigger_echo():
    # Varmistetaan etta TRIG on pois paalta
    PIN_TRIG.write_digital(True)
    sleep(1)
    # Kaynnistetaan TRIG
    PIN_TRIG.write_digital(False)
#    sleep(10)
    # Pistetaan taas TRIG pois paalta
#    PIN_TRIG.write_digital(False)


# Mittaa kaiun pituus
def poll_duration():
    # Odotetaan etta ECHO pin aktivoituu
    start_time = running_time()
    # While pyorii kunnes ECHO pin aktivoituu (tai menee liian pitkaan)
    while not PIN_ECHO.read_digital():
        if running_time() - start_time > 5000:
            # Palautetaan oletusarvo koska ECHO pinilla meni liian pitkaan
            return -1.0 * 2.0 * 29.1

    # ECHO pin on aktiivinen, mitataan kuinka kauan
    start_time = running_time()
    # While pyorii kunnes ECHO pin epaaktivoituu (tai menee liian pitkaan)
    while PIN_ECHO.read_digital():
        if running_time() - start_time > 5000:
            # Palautetaan oletusarvo koska ECHO pinilla meni liian pitkaan
            return 1000.0 * 2.0 * 29.1

    # Palautetaan kuinka pitkaan meni (nykyhetki - aloitushetki)
    return running_time() - start_time


# Muuta kaiku-aika mitatuksi etaisyydeksi
def duration_to_distance(duration):
    # Lasketaan matka perustuen kaiun kestoon
    return (duration / 2.0) / 29.1


# Nayta etaisyys LED-naytolla
def show_distance(distance):
    # Muutetaan distance ledien maaraksi
    # Aluksi lasketaan matka MIN_DISTin jalkeen
    distance_from_min = distance - MIN_DIST
    # Muutetaan distance MINista valilta 0..DIST valille 0..5
    leds = min(5, max(0, 5.0 * distance_from_min / DIST))
    # Lasketaan kokonaisten ledien maara, varmistetaan etta niita on maksimissaan 4
    led_count = min(4, int(leds))
    # Lasketaan viimeisen ylimaaraisen ledin kirkkaus (ylijaama kokonaisista)
    last_led_brightness = int(min(9, round(9 * (leds - led_count))))
    # Siivotaan ruutu
    display.clear()
    # Laitetaan led_count maara ledeja paalle
    for i in range(led_count):
        set_pixel_column(i, i + 1, 9)
    # Laitetaan viela viimeinen led paalle (mikali sen kirkkaus on >0)
    if last_led_brightness > 0:
        set_pixel_column(led_count, led_count + 1, last_led_brightness)


# Aseta LED-kolumni "x" kirkkaudeksi "brightness" korkeudella "height"
# Eli "set_pixel_column(1, 2, 3)" tekee seuraavan:
# - Pistaa ledeja paalle kolumnissa 1, eli toiset ledit vasemmalta (0 on vasen)
# - Pistaa niita 2 paalle, eli kaksi alinta (aloitetaan alhaalta)
# - Pistaa ne ledit kirkkaudelle 3 (min kirkkaus on 0, max on 9)
def set_pixel_column(x, height, brightness):
    # Pistetaan pixeleita paalle pystysuunnassa heightin verran alhaalta ylos
    for i in range(5):
        # i on "kuinka mones led", joten pistetaan paalle vain < height ledit
        if i < height:
            # Laitetaan paalle led kolumnissa x alkaen alhaalta (4)
            display.set_pixel(x, 4 - i, brightness)


# Toistetaan funktiota "loop" 50 kertaa sekunnissa
while True:
    loop()
    # "Nukutaan" 20 millisekuntia (0.02 sekuntia) jokaisen loopin valissa
    # (kun nukumme 0.02s, loopin taajuus on 50 Hz, silla 1 / 0.02s = 50Hz)
    sleep(20)
