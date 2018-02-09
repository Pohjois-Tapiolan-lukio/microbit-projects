from microbit import *
import music

# Soitettavien melodioiden nimet
melodia_nimet = [
    "DADADADUM", "ENTERTAINER", "PRELUDE", "ODE",
    "NYAN", "RINGTONE", "FUNK", "BLUES", "BIRTHDAY",
    "WEDDING", "FUNERAL", "PYTHON", "BADDY", "CHASE"
]

# Melodiat (micro:bitin sisäänrakennetut) samassa järjestyksessä kuin nimet
melodiat = [
    music.DADADADUM, music.ENTERTAINER, music.PRELUDE, music.ODE,
    music.NYAN, music.RINGTONE, music.FUNK, music.BLUES, music.BIRTHDAY,
    music.WEDDING, music.FUNERAL, music.PYTHON, music.BADDY, music.CHASE
]


def soita_melodia(indeksi): # Alkaa soittamaan melodiaa ja näyttää sen nimen ruudulla
    global melodiat, melodia_nimet # Käytetään näitä globaaleja (eli funktion ulkopuolisia) muuttujia

    # Näytä teksti "N. XYZW" missä N on melodian indeksi, ja XYZW sen nimi
    # Delay = 120 (oletus: 150) ja loop = True (oletus: False) saavat tekstin pyörimään hieman nopeammin ja toistumaan kunnes se muutetaan
    # Wait = False tekee niin, ettei ohjelma pysähdy tähän, vaan jatkaa eteenpäin samalla kun näyttää tekstin ruudulla
    display.scroll(str(indeksi + 1) + ". " + melodia_nimet[indeksi], delay = 120, loop = True, wait = False)

    music.stop() # Pysäytä musiikki
    sleep(500) # 0.5s (500 millisekuntia) tauko, hiljaisuus ennen seuraavaa melodiaa
    music.play(melodiat[indeksi], wait = False) # Melodia soimaan


melodia_indeksi = 0 # Tällä hetkellä soivan melodian indeksi, muutetaan kun vaihdetaan melodiaa
soita_melodia(melodia_indeksi) # Ensimmäinen melodia soimaan

while True: # Aloitetaan toistolause

    if button_a.was_pressed(): # Kun A:ta painetaan, siirrytään edelliseen melodiaan
        melodia_indeksi -= 1 # Muutetaan indeksiä taaksepäin
        if melodia_indeksi < 0: # Jos indeksi meni negatiiviseksi...
            melodia_indeksi = len(melodiat) - 1 # Siirretään indeksi ympäri, listan viimeiseksi indeksiksi
        soita_melodia(melodia_indeksi) # Soitetaan melodia uudella indeksillä

    if button_b.was_pressed(): # Kun B:tä painetaan, siirrytään seuraavaan melodiaan
        melodia_indeksi += 1 # Muutetaan indeksiä eteenpäin
        if melodia_indeksi >= len(melodiat): # Jos indeksi meni yli listan pituuden...
            melodia_indeksi = 0 # Siirretään indeksi toiselle puolelle listaa, ensimmäiseen indeksiin
        soita_melodia(melodia_indeksi) # Soitetaan melodia uudella indeksillä

    if accelerometer.current_gesture() == "shake": # Kun micro:bitiä heilutetaan, pysäytä melodia
        music.stop() # Pysäytä melodia
        display.clear() # Tyhjennä ruutu (ettei melodian nimi enään näy)
