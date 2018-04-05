# Tämä ohjelma näyttää hymynaamaa kunnes painetaan nappia, odottaa hetken, ja lausuu kuulokkeissa määrän painalluksia.

# Kytke kaiuttin microbitin pinneihin 0 ja 1.
import speech # Kerrotaan Pythonille että käytämme puhumisominaisuuksia (ei sisälly alempaan)
from microbit import * # Kerrotaan Pythonille että käytämme microbitin sisäänrakennettuja muitakin toimintoja

display.show(Image.HAPPY) # Näytetään hymynaamaa
while True: # Aloitetaan toistosilmukka
    if button_a.is_pressed(): # Mikäli nappia painettiin...
        display.clear() # Tyhjennetään ruutu
        sleep(5000) # Odotetaan 5 sekuntia
        display.show(Image.MUSIC_QUAVER) # Näytetään musikaalinen kuva, viitaten siihen että micro:bit puhuu nyt
        painallukset = button_a.get_presses() + 1 # Painalluksien määrään pitää laskea myös se jolla siirryimme tähän if-lausekkeeseen (+ 1)
        speech.say(str(painallukset)) # micro:bit sanoo luvun, str muuttaa luvun tekstiksi
        display.show(Image.HAPPY) # Näytetään taas hymynaamaa
