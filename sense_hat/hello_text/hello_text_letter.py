from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

sense.show_letter("B", red)
sleep(1)
sense.show_letter("E", blue)
sleep(1)
sense.show_letter("E", green)
sleep(1)
sense.show_letter("R", black, white)
sleep(1)
sense.clear()
