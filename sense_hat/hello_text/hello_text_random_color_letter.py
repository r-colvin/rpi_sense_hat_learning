from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

r = randint(0,255)
sense.show_letter("B", (r, 0, 0))
sleep(1)

r = randint(0,255)
sense.show_letter("E", (0, 0, r))
sleep(1)

r = randint(0,255)
sense.show_letter("E", (0, r, 0))
sleep(1)

sense.show_letter("R", (0, 0, 0), (255, 255, 255))
sleep(1)
sense.clear()
