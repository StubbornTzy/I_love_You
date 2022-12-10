import turtle as tur
import colorsys as cs

tur.setup(600,600)
tur.speed(0)
tur.tracer(100)
tur.screensize(70)
tur.bgcolor('black')
for j in range(25):
    for i in range(15):
        tur.color(cs.hsv_to_rgb(i/25,j/25,1))
        tur.right(90)
        tur.circle(200-j*4,90)
        tur.left(90)
        tur.circle(200-j*4,90)
        tur.right(100)
        tur.circle(5,24)
tur.hideturtle()
tur.done