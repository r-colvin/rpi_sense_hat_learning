from sense_hat import SenseHat

sense = SenseHat()

white = (255, 255, 255)
blue = (0, 0, 255)

message = "#CloudBeerKarlskrona"

speed = 0.05

while True:
    sense.show_message(message, speed, text_colour=white, back_colour=blue)
