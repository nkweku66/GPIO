from gpiozero import LED, Button
from signal import pause
from subprocess import call

led = LED(17)
button = Button(2)

def print_thing():
    print ("restarting...")

button.when_pressed = print_thing

pause()
