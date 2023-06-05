import colorsys
import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('black')
t.speed(100)


def Diamond(d):
    t.left(60)
    for i in range(1):
        t.forward(d)
        t.right(120)
        t.forward(d)
        t.right(60)
        t.forward(d)
        t.right(120)
        t.forward(d)
        t.right(120)


t.penup()
t.goto(0, 0)
t.pendown()
h = 1
n = 10
for k in range(80):
    h += 0.5 / n
    c = colorsys.hls_to_rgb(h, 0.4, 1)
    t.pencolor(c)
    t.circle(k)
    t.penup()
    t.forward(4)
    t.pendown()
    t.right(2)

t.penup()
t.goto(0, 0)
t.pendown()
h = 1
n = 10
t.left(40)
for k in range(80):
    h += 0.5 / n
    c = colorsys.hls_to_rgb(h, 0.4, 1)
    t.pencolor(c)
    t.circle(k)
    t.penup()
    t.forward(4)
    t.pendown()
    t.right(2)

t.penup()
t.goto(0, 0)
t.pendown()
h = 1
n = 10
t.left(40)
for k in range(80):
    h += 0.5 / n
    c = colorsys.hls_to_rgb(h, 0.4, 1)
    t.pencolor(c)
    t.circle(k)
    t.penup()
    t.forward(4)
    t.pendown()
    t.right(2)
t.hideturtle()
turtle.done()
