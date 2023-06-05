import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.pencolor('brown')
for i in range(17):
    t.penup()
    t.left(10)
    t.pendown()
    for k in range(30):
        t.pensize((30-k) / 2)
        t.forward(4)
    for k in range(30):
        t.backward(4)



