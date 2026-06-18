from gpiozero import LED
from gpiozero import Button
from time import sleep

ledR = LED(14)
button = Button(15)

while True:
 if button.is_pressed:
  print("Button is pressed")
  ledR.on()
 else:
  print("Button is not pressed")
  ledR.off()
 sleep(0.05)

#hahaha
