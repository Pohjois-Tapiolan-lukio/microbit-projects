from microbit import *
import radio

radio.on() # Radio paalle
radio.config(channel = 50) # Valitse kanava 0-100 valilta

potentiometri = 0 # Alustetaan potentiometri 0:n

while True:
    potentiometri_uusi = pin0.read_analog() # Luetaan potentiometrin arvo

    if abs(potentiometri - potentiometri_uusi) > 30: # Uusi lukema on eri, potentiometria on liikutettu -> Lahetetaan viesti!
        radio.send(str(potentiometri)) # Lahetetaan potentiometrin arvo tekstina

        potentiometri = potentiometri_uusi # Paivitetaan potentiometrin arvo seuraavaa kertaa varten

    sleep(30) # Nukutaan 30 millisekuntia jottei toistolause mene liian nopeasti