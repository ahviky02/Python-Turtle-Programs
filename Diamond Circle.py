import colorsys
import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('black')
t.speed(100)


def Diamond():
    t.left(60)
    for i in range(1):
        t.forward(70)
        t.right(120)
        t.forward(70)
        t.right(60)
        t.forward(70)
        t.right(120)
        t.forward(70)
        t.right(120)


t.penup()
t.goto(0, 150)
t.pendown()
h = 1
n = 10
for k in range(122):
    t.forward(12)
    t.right(3)
    Diamond()
    h += 0.5 / n
    c = colorsys.hls_to_rgb(h, 0.4, 1)
    t.pencolor(c)

t.hideturtle()
turtle.done()
