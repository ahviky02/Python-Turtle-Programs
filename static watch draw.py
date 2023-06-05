import turtle


t=turtle.Turtle()
s=turtle.Screen()

s.bgcolor("black")
t.left(90)
t.speed(0)

def draw(l):
    if(l<10):
        return 
    else :

        t.pensize(2)
        t.pencolor("#FFCCCC")
        t.forward(l)
        t.left(30)
        draw(3*l/4)
        t.right(60)
        draw(3*l/4)
        t.left(30)
        t.pensize(2)
        t.backward(l)

draw(20)
t.right(90)

def draw(l):
    if(l<10):
        return
    else:
        t.pensize(2)
        t.pencolor("green")
        t.forward(l)
        t.left(30)
        draw(3*l/4)
        t.right(60)
        draw(3*l/4)
        t.left(30)
        t.pensize(2)
        t.backward(l)
draw(20)
t.left(270)

def draw(l):
    if (l<10):
        return
    else:
        t.pensize(2)
        t.pencolor("red")
        t.forward(l)
        t.left(30)
        draw(3*l/4)
        t.right(60)
        draw(3*l/4)
        t.left(30)
        t.pensize(2)
        t.backward(l)

draw(20)
t.right(90)


def draw(l):
    if (l<10):
        return
    else:
        t.pensize(2)
        t.pencolor("blue")
        t.forward(l)
        t.left(30)
        draw(3*l/4)
        t.right(60)
        draw(3*l/4)
        t.left(30)
        t.pensize(2)
        t.backward(l)

draw(20)

def draw(l):
    if (l<10):
        return
    else:
        t.pensize(2)
        t.pencolor("green")
        t.forward(l)
        t.left(30)
        draw(3*l/4)
        t.right(60)
        draw(3*l/4)
        t.left(30)
        t.pensize(2)
        t.backward(l)


draw(40)
t.right(90)


def draw(l):
    if (l<10):
        return
    else:
        t.pensize(2)
        t.pencolor("red")
        t.forward(l)
        t.left(30)
        draw(3*l/4)
        t.right(60)
        draw(3*l/4)
        t.left(30)
        t.pensize(2)
        t.backward(l)

draw(40)
t.left(270)

def draw(l):
    if (l<10):
        return
    else:
        t.pensize(2)
        t.pencolor("blue")
        t.forward(l)
        t.left(30)
        draw(3*l/4)
        t.right(60)
        draw(3*l/4)
        t.left(30)
        t.pensize(2)
        t.backward(l)

draw(40)
t.right(90)

2
def draw(l):
    if (l<10):
        return
    else:
        t.pensize(2)
        t.pencolor("white")
        t.forward(l)
        t.left(30)
        draw(3*l/4)
        t.right(60)
        draw(3*l/4)
        t.left(30)
        t.pensize(2)
        t.backward(l)

draw (40)
s.exitonclick()