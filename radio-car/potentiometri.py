from microbit import *
import radio

radio.on() # Radio päälle
radio.config(channel = 50) # Valitse kanava 0-100 väliltä

kaasu = 0
suunta = 0

while True:
    kaasu_uusi = pin0.read_analog() # Luetaan potentiometrin arvo
    suunta_uusi = pin1.read_analog() # Luetaan potentiometrin arvo

    if kaasu != kaasu_uusi: # Uusi lukema on eri, kaasua on muutettu -> Lähetetään viesti!
        radio.send("k:" + str(kaasu)) # Lähetetään kaasun arvo tekstinä
        sleep(10) # Nukutaan 10 millisekuntia jottei lähetetä viestjä liikaa
    if suunta != suunta_uusi: # Uusi lukema on eri, suuntaa on muutettu -> Lähetetään viesti!
        radio.send("s:" + str(suunta)) # Lähetetään suunnan arvo tekstinä
        sleep(10) # Nukutaan 10 millisekuntia jottei lähetetä viestjä liikaa

    kaasu = kaasu_uusi # Päivitetään kaasun arvo seuraavaa kertaa varten
    suunta = suunta_uusi # Päivitetään suunnan arvo seuraavaa kertaa varten
