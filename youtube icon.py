import turtle


t=turtle.Turtle()
s=turtle.Screen()
t.pensize(2)
s.bgcolor("black")

t.pencolor("red")
t.penup()
t.goto(0,50)
t.pendown()

def r():
    for i in range(10):
        t.forward(5)
        t.right(9)
t.fillcolor("red")
t.begin_fill()
t.forward(90)
r()
t.forward(90)
r()
t.forward(170)
r()
t.forward(90)
r()
t.forward(90)
t.end_fill()
t.hideturtle()

t1=turtle.Turtle()
t1.pencolor("white")

t1.fillcolor("white")
t1.begin_fill()
t1.penup()
t1.goto(10,-27)
t1.pendown()
t1.forward(33)
t1.right(150)
t1.forward(60)
t1.right(120)
t1.forward(60)
t1.right(120)
t1.forward(60)
t1.right(120)
t1.forward(40)
t1.end_fill()
t1.hideturtle()
turtle.done()

