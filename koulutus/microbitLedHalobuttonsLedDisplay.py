from microbit import *

while True:
    gesture = accelerometer.current_gesture()
    
    if gesture == "shake":
        display.show(Image.ANGRY) # Gestures: face up, freefall, up, down, left, right, ..
        sleep(500)
        display.clear()
        
    if button_a.is_pressed():
        display.scroll("Terve")
    
    elif button_b.was_pressed():
        display.show(Image.HAPPY)
        sleep(2000)
        display.clear()
    
    else:
        display.show(Image.HEART)
        