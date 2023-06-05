from turtle import *
import turtle as turt 
turt.title("Official_Coding")
def petals(t, radius, angle):
    for i in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)
        
def flowers(t, n, radius, angle):
    for i in range(n):
        petals(t, radius, angle)
        t.left(360.0 / n)
        
def move(t, length):
    wind = turt.Screen()
    wind.bgcolor("black")
    t.pu()
    t.fd(length)
    t.pd()
    
wd = turt.Turtle()
wd.speed(1)

wd.color("lime")
wd.shape("turtle")
move(wd, -150)
wd.begin_fill()
flowers(wd, 9, 150.0, 60.0)
wd.end_fill()

wd.color("cyan")
move(wd, 150)
wd.begin_fill()
flowers(wd, 11, 40.0, 80.0)
wd.end_fill()

wd.color("violet")
move(wd, 150)
wd.begin_fill()
flowers(wd, 15, 80.0, 60.0)
wd.end_fill()

turt.mainloop()