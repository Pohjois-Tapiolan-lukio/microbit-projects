# Gamepad
Raspberry Pi osuuden löydät [täältä](https://github.com/Pohjois-Tapiolan-lukio/raspberry_pi-projects/tree/master/projects/gamepad#python-sarjaliikennekuuntelija)

## Yhteenveto
Tässä projektissa opetetaan Microbitin ja Linux-laitteen välisen
_sarjaliikenne_-kommunikoinnin perusteet.

Tämä kansio sisältää vain Microbittiin liittyvät ohjeet.

## Tarvittavat osat
- Microbit & USB-johto
- Jotain seuraavista:
    - Nappeja
    - Joystickeja
- 1KΩ vastuksia
> (vaatii lisätutkimusta: liian suuri pulldown-vastus tuottaa ongelmia
> `read_digital`-metodin kanssa)
- Hyppylankoja jne.
> Voit hyödyntää Raspberryn 40-pinnistä `T-Cobbler`-kaapelia, jos haluat
> käyttää kytkentäalustaa

## Ohjeet

### Napit ja joystickit
Lue napeista ja joystickeista [<i>täältä</i>](https://github.com/Pohjois-Tapiolan-lukio/arduino-projects/tree/master/gamepad#ohjeet)

### Microbitin ohjelmointi MicroPythonilla
> Ohjelman rakenne on sama kuin Arduinolla

> Pinnien diagrammi
![](microbitpinout.png)
Määritellään napin tai joystickin pinni(t)
```python
NAPPI = pin[napin pinnin numero]

# Joystickin akselien pinnien pitaa olla analogisia syotteita (ANALOG IN)
JOYSTICK_X = pin[joystickin horisontaalisen akselin pinnin numero]
JOYSTICK_Y = pin[vertikaalisen akselin pinnin numero]
JOYSTICK_THUMB = pin[joystickin napin pinnin numero]
```
