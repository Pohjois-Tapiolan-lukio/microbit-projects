# Microbit controlled ledStrip

Demossa ohjataan microbitin avulla RGB-led-nauhaa

## Kytkentä

Microbit --> RGB-lednauha

D0 --> Din eli data in

3V --> +5V lednauhan käyttöjännite

GND --> 0V tai GND

## Lähetin

Lähetin microbit lukee kiihtyvyysanturin x,y,z- arvot asteikolta 0 ...1023 ja muuntaa ne lednauhan RGB -arvoiksi välille 0 ...255. Napeista A ja B voi muuttaa lednauhan ledien lukumäärää. Tämän jälkeen arvot lähetetään vastaanotin microbitille.

![](images/img1.png)

![](images/img2.png)

## Vastaanotin
Vastaanotin lukee radioviestinä saapuneita RGB-arvoja ja aktiivisten ledien lukumäärän ja kirjoittaa arvot lednauhaan.

![](images/img3.png)

![](images/img4.png)

![](images/img5.png)

![](images/img6.png)

## License
[MIT](https://choosealicense.com/licenses/mit/)
