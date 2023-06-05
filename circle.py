import turtle
import colorsys

t= turtle.Turtle()
s=turtle.Screen()
t.speed(0)
s.bgcolor("black")
n=70
h=0
for i in range(360):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n
    t.color(c)
    t.left(2)
    for k in range(5):
        t.forward(300)
        t.left(120)
        