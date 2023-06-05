import colorsys
from tkinter.font import NORMAL
import turtle


t1=turtle.Turtle()
s1=turtle.Screen()
t1.pensize(2)
s1.bgcolor("darkgray")

t1.hideturtle()
t1.circle(100)
t1.penup()
t1.goto(0,5)
t1.pendown()
t1.circle(95)

t1.penup()
t1.goto(-70,120)
t1.pendown()

t1.write("      ahvi02",font=("Ariel",16,'normal'))

t1.penup()
t1.goto(-25,95)
t1.pendown()

# t1.write("subscribe",font=("Ariel",13,'normal'))

t1.penup()
t1.goto(-5,15)
t1.pendown()

t1.forward(10)
t1.left(90)
t1.forward(25)
t1.right(30)
for i in range (270):
    t1.forward(0.1)
    t1.left(1)
    
t1.right(60)
t1.forward(25)

t1.left(180)
t1.penup()
t1.goto(55,177)
t1.pendown()
t1.forward(80)
for i in range(180):
    t1.forward(1)
    t1.left(1)
t1.forward(80)

t1.goto(-45,187)
t1.backward(70)
for i in range(180):
    t1.backward(0.74)
    t1.right(1)

t1.backward(70)



turtle.done()