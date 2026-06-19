from gpiozero import LED
from gpiozero import Button
from time import sleep
import random

ledR = LED(14)
ledG = LED(23)
ledY = LED(24)
button1 = Button(15)
button2 = Button(18)
while True:
    time = random.uniform(3, 5)
    sleep(time)
    ledR.on()
    while True:
      if button1.is_pressed:
        ledY.on()
        sleep(0.4)
        ledY.off()
        sleep(0.4)
        ledY.on()
        sleep(0.4)
        ledY.off()
        sleep(0.4)
        ledY.on()
        sleep(0.4)
        ledY.off()
        sleep(0.4)
        print("p1 win")
        break
      elif button2.is_pressed:
        ledG.on()
        sleep(0.4)
        ledG.off()
        sleep(0.4)
        ledG.on()
        sleep(0.4)
        ledG.off()
        sleep(0.4)
        ledG.on()
        sleep(0.4)
        ledG.off()
        sleep(0.4)
        print("p2 win")
        break
    ledR.off()
    
    sleep(1)




#hahaha
