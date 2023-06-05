import turtle

t1 = turtle.Turtle()
s = turtle.Screen()
t1.pensize(25)
s.bgcolor('black')
t1.pencolor('brown')

# Main Branch
t1.penup()
t1.goto(0, -200)
t1.pendown()
t1.pensize(30)
t1.left(90)
t1.forward(200)


# p1.1
def prt1(pensize, dis, ang, t):
    t.pensize(pensize)
    t.left(ang)
    t.forward(dis)
    leaf(5,30, t)
    t.pencolor('brown')
    prt2(pensize * 3 / 4, dis * 3 / 4, ang, t)


# p1.2
def prt2(pensize, dis, ang, t):
    t.pensize(pensize)
    t.left(ang)
    t.forward(dis)
    prt3(pensize * 1 / 2, dis * 1 / 2, ang * 1 / 2, t)
    t.back(dis)
    t.pensize(pensize)
    t.right(ang + 10)
    t.forward(dis)
    prt3(pensize * 1 / 2, dis * 1 / 2, ang * 1 / 2, t)
    t.back(dis)
    t.pensize(pensize)
    t.left(ang - 30)
    t.forward(dis)
    prt3(pensize * 1 / 2, dis * 1 / 2, ang * 1 / 2, t)


# p1.3
def prt3(pensize, dis, ang, t):
    t.pensize(pensize)
    t.left(ang)
    t.forward(dis)
    leaf(pensize / 2, dis / 2,  t)
    t.pencolor('brown')
    t.pensize(pensize)
    t.back(dis)
    t.right(ang + 10)
    t.forward(dis)
    leaf(pensize / 2, dis / 2,  t)
    t.pencolor('brown')
    t.pensize(pensize)
    t.back(dis)
    t.right(ang)
    t.forward(dis)
    leaf(pensize / 2, dis / 2, t)
    t.pencolor('brown')
    t.pensize(pensize)
    t.back(dis)
    t.left(ang + 10)


def leaf(pensize, dis, t):
    if dis > 20:
        t.pencolor('lime')
        t.pensize(pensize)
        t.left(40)
        t.forward(dis)
        leaf(pensize * 3 / 4, dis * 3 / 4, t)
        t.back(dis)
        t.right(40)
        t.forward(dis)
        leaf(pensize * 3 / 4, dis * 3 / 4, t)
        t.back(dis)
        t.right(40)
        t.forward(dis)
        leaf(pensize * 3 / 4, dis * 3 / 4, t)
        t.back(dis)
        t.left(40)

    else:
        return

prt1(20, 150, 70, t1)


t5 = turtle.Turtle()
t5.pencolor('brown')
t5.pensize(15)
t5.left(135)
t5.forward(100)
leaf(5,30, t5)
prt3(15 * 1 / 2, 100 * 1 / 2, 70 * 1 / 2, t5)

t4 = turtle.Turtle()
t4.pencolor('brown')
t4.pensize(25)
t4.left(90)
t4.forward(80)
t4.right(30)
t4.forward(80)
t4.left(40)
prt3(17 * 1 / 2, 120 * 1 / 2, 70 * 1 / 2, t4)
t4.pensize(20)
t4.forward(50)
t4.right(40)
prt2(20 * 3 / 4, 150 * 3 / 4, 70, t4)

t3 = turtle.Turtle()
t3.pencolor('brown')
t3.pensize(25)
t3.left(90)
t3.forward(70)
t3.right(10)
prt1(20, 130, 50, t3)

t2 = turtle.Turtle()
t2.pencolor('brown')

t2.right(40)
prt1(20, 150, 70, t2)
t2.back(200 * 1 / 2)
t2.right(80)
t2.pensize(15)
t2.forward(90)
prt3(17 * 1 / 2, 120 * 1 / 2, 70 * 1 / 2, t2)

turtle.done()
