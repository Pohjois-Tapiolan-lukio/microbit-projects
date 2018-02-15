# Micro:bitin heilutus nayttaa kolmen kuvan animaation ruudulla. Animaatiossa on nelio joka pienenee.
from microbit import *

# Luodaan kuvat. Kaksoispiste toimii rivien erottajana, numerot viittaavat pikselin kirkkauteen (0-0)
iso_nelio = Image("99999:"
                  "99999:"
                  "99999:"
                  "99999:"
                  "99999")
keskikokoinen_nelio = Image("02220:"
                            "29992:"
                            "29992:"
                            "29992:"
                            "02220")
pieni_nelio = Image("00000:"
                    "00200:"
                    "02920:"
                    "00200:"
                    "00000")

# Luodaan animaatio. Tama on taulukko joka sisaltaa jokaisen aiemminluoduista kuvista, esitysjarjestyksessa.
animaatio = [iso_nelio, keskikokoinen_nelio, pieni_nelio]

while True: # Aloitetaan toisto
    if accelerometer.current_gesture() == "shake": # Jos microbittia heilutetaan...
        # Animaatio alkaa...
        for kuva in animaatio: # Toistetaan jokaiselle kuvalle jarjestyksessa...
            display.show(kuva) # Nayta kuva
            sleep(500) # Odota 500ms (eli 0.5 sekuntia)
        # Animaatio naytetty!
    # Toistolauseke loppuu, palataan alkuun
