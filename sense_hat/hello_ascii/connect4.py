from sense_hat import SenseHat

sense = SenseHat()

r = (255, 0, 0)
b = (0, 0, 255)
e = (0, 0, 0)

image = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,r,e,e,e,e,e,
b,b,b,b,r,e,e,e,
r,r,b,b,r,e,e,e
]

sense.set_pixels(image)
