import colorsys
import turtle
t= turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.speed(1000)
n= 100
h=0

for i in range(360):
    c= colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n
    t.color(c)
    for k in range(2):
        t.left(250)
        t.forward(i*3)
        for z in range(3):
            t.left(144)
            t.forward(22)
            for z in range(3):
                t.left(10)
                t.forward(22)
                