import colorsys
import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')

t.speed(1000)
c = ['red', 'lime', 'cyan', 'violet']
for i in range(2000):
    t.pencolor(c[i % 4])
    t.forward(i + 60)
    t.right(91)

turtle.done()
