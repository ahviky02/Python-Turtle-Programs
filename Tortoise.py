
import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('black')
t.penup()
t.goto(0, -200)
t.shape('turtle')
t.speed(3)

t.pencolor('black')
t.color('lime')
t.pensize(3)
t.turtlesize(10)
t.forward(100)

for i in range (100):
    t.circle(200)
turtle.done()
