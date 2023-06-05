from cmath import pi
import turtle


h=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('cyan')
h.pensize(2)
h.penup()
h.pendown()
h.pencolor('navy')
def round(a,d,r):
    for i in range(r):
        h.right(a)
        h.forward(d)
        
def round1(a,d,r):
    for i in range(r):
        h.left(a)
        h.forward(d)
t1=turtle.Turtle()
t1.forward(700)
t1.backward(1400)
t1.penup()
t1.goto(0,0)
t1.pendown()
t1.right(90)
t1.backward(500)
t1.forward(1000)
h.left(80)


t2=turtle.Turtle()
t2.hideturtle()
t2.pensize(2)
t2.penup()
t2.goto(-300,300)
t2.pendown()
t2.write('-1<=sin(x)<=1',font=('Arial',25,'normal'))

t2.penup()
t2.goto(60,0)
t2.pendown()
t2.write('π/2',font=('Arial',13,'normal'))

t2.penup()
t2.goto(120,0)
t2.pendown()
t2.write('π',font=('Arial',13,'normal'))

t2.penup()
t2.goto(170,0)
t2.pendown()
t2.write('3π/2',font=('Arial',13,'normal'))

t2.penup()
t2.goto(240,0)
t2.pendown()
t2.write('2π',font=('Arial',13,'normal'))

t2.penup()
t2.goto(300,0)
t2.pendown()
t2.write('5π/2',font=('Arial',13,'normal'))

t2.penup()
t2.goto(360,0)
t2.pendown()
t2.write('3π',font=('Arial',13,'normal'))



t2.penup()
t2.goto(-60,0)
t2.pendown()
t2.write('π/2',font=('Arial',13,'normal'))

t2.penup()
t2.goto(-130,0)
t2.pendown()
t2.write('π',font=('Arial',13,'normal'))

t2.penup()
t2.goto(-170,0)
t2.pendown()
t2.write('3π/2',font=('Arial',13,'normal'))

t2.penup()
t2.goto(-230,0)
t2.pendown()
t2.write('2π',font=('Arial',13,'normal'))

t2.penup()
t2.goto(-300,0)
t2.pendown()
t2.write('5π/2',font=('Arial',13,'normal'))

t2.penup()
t2.goto(-370,0)
t2.pendown()
t2.write('3π',font=('Arial',13,'normal'))

t2.penup()
t2.goto(0,60)
t2.pendown()
t2.write(' 1',font=('Arial',13,'normal'))

t2.penup()
t2.goto(0,-70)
t2.pendown()
t2.write(' -1',font=('Arial',13,'normal'))



for i in range(2):
    round(2,3,30)
    round(4,0.7,10)
    round(2,3,30)
    round1(2,3,30)
    round1(4,0.7,10)
    round1(2,3,30)

h.penup()
h.goto(0,0)
h.pendown()
h.left(180)

for i in range(2):
    round(2,3,30)
    round(4,0.7,10)
    round(2,3,30)
    round1(2,3,30)
    round1(4,0.7,10)
    round1(2,3,30)
    



turtle.done()   







