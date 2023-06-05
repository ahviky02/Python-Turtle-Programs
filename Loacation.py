import colorsys
import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')

t.speed(100)
t.pencolor('cyan')
t.penup()
t.goto(0, -200)
t.pendown()


for i in range(50):
    t.circle(i)
    t.penup()
    t.left(90)
    t.forward(1)
    t.right(90)
    t.pendown()

for i in range(7):
    t.circle(50)
    t.penup()
    t.left(90)
    t.forward(1)
    t.right(90)
    t.pendown()

for i in range(50):
    t.circle(50-i)
    t.penup()
    t.left(90)
    t.forward(1)
    t.right(90)
    t.pendown()

turtle.done()
