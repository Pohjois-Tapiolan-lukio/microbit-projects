# Add your Python code here. E.g.
from microbit import *
from neopixel import NeoPixel
import radio

PIXELS = 24

TARGET_COLOR = [0,16,0]
OBJECT_COLOR = [64,0,0]
BOTH_COLOR = [128,128,0]

INITIAL_SPEED = 100
INCREMENT = 10

LOWER_LIMIT = 10
UPPER_LIMIT = 14

ring = NeoPixel(pin0, PIXELS)

def game():
    score = 0
    position = 0
    alive = True
    speed = INITIAL_SPEED
    
    while alive:
        position = move(position, PIXELS)
        ring.show()
        sleep(speed)
        
        if button_a.get_presses() > 0:
            if LOWER_LIMIT < position < UPPER_LIMIT:
                score += 1
                display.show(str(score % 10))
                speed -= INCREMENT
            else:
                alive = False
    
    display.show(Image.SAD)
    sleep(2000)
    
    while button_b.get_presses() == 0:
        display.scroll(str(score))
            
        


def move(current, loop_length):
    if LOWER_LIMIT < current < UPPER_LIMIT:
        ring[current] = TARGET_COLOR
    else:
        ring[current] = [0,0,0]
        
    new = (current + 1) % PIXELS
    
    if LOWER_LIMIT < new < UPPER_LIMIT:
        ring[new] = BOTH_COLOR
    else:
        ring[new] = OBJECT_COLOR
    
    return new

while True:
    game()
