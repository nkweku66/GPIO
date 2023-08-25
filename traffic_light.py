from gpiozero import LED, Button
from time import sleep


led = LED(18)
led2 = LED(21)
led3 = LED(20)

button = Button(2)
while True:
    led3.on()
    button.wait_for_press()
    led3.off()
    led.on()
    sleep(8)
    led.off()
    led2.on()
    sleep(10)
    led2.off()
    led3.on()
    sleep(10)
    #button.wait_for_release()
    
#button.when_pressed = led1.on
#button.when_released = led2.on

#pause()
