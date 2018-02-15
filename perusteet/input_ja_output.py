# Kytke nappi pietsokaiutin pinniin 1 ja gnd-porttiin. Napin voit rakentaa kytkemalla johdon
# maadoitukseen, ja koskettamalla digiporttia 0.

from microbit import * # Kerro Pythonille että käytetään microbitin ominaisuuksia (esim. pin0)

while True: # Avaa silmukka
    if pin0.is_touched(): # Jos pin0:n kosketaan...
        pin1.write_digital(1) # Pistetään pin1:een virta päälle
    else: # Jos pin0:n ei koskettukaan...
        pin1.write_digital(0) # PIstetään pin1:n virta pois päältä
    # Ei enempää suoritettavaa, palaa silmukan alkuun