import turtle

t = turtle.Turtle()
s = turtle.Screen()

t.speed(1000)
t.pensize(2)
s.bgcolor('black')

t.penup()
t.goto(0, 100)
t.pendown()

color = ['cyan', 'green', 'blue', 'yellow',
         'red', 'lime', 'navy', 'white', 'brown', 'purple']

for i in range(1000):
    t.fillcolor(color[i % 10])
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    t.right(20)
    t.penup()
    t.forward(67)
    t.pendown()
