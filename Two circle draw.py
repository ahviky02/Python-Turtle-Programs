import turtle
import colorsys

t= turtle.Turtle()
s=turtle.Screen()
t.speed(0)
s.bgcolor("black")
n=70
h=0
for i in range(3600):
   
    h+=1/n
    t.color("aqua")
    t.circle(i*10)
    t.right(180)
    t.circle(1*10)
        
