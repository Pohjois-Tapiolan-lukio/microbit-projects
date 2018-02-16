from microbit import *
import radio

radio.on() # Radio paalle
radio.config(channel = 50) # Valitse kanava 0-100 valilta

potentiometri = (0, 0, 0) # Alustetaan potentiometri 0:n

while True:
    potentiometri_uusi = (pin0.read_analog(), pin1.read_analog(), pin2.read_analog()) # Luetaan potentiometrin arvo

    if potentiometri != potentiometri_uusi: # Uusi lukema on eri, potentiometria on liikutettu -> Lahetetaan viesti!
        r, g, b = potentiometri_uusi # Jaetaan potentiometrien lukemat kolmeen uuteen muuttujaan (eli r on pin0, g on pin1 ja b on pin2)
        radio.send(r + "," + g + "," + b) # Lahetetaan potentiometrin arvo tekstina

    potentiometri = potentiometri_uusi # Paivitetaan potentiometrin arvo seuraavaa kertaa varten

    sleep(30) # Nukutaan 30 millisekuntia jottei toistolause mene liian nopeasti
