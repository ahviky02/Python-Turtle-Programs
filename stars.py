



import colorsys
import turtle 


t=turtle.Turtle()
s=turtle.Screen()

s.bgcolor("black")
t.speed(0)


for i in range(360):
    t.color("cyan")
    t.left(8)
    t.forward(100)
    t.right(175)
    for k in range(4):
        t.forward(i*1)
        t.left(6)  

        
        