let ring: neopixel.Strip = null
ring = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)
basic.forever(function () {
    ring.showRainbow(1, 360)
    ring.show()
    basic.pause(100)
})
