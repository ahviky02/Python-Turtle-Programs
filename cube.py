import colorsys
import turtle


t1=turtle.Turtle()
s1=turtle.Screen()
t1.pensize(2)
s1.bgcolor("darkgray")

def square():
    for i in range(4):
        t1.forward(300)
        t1.right(90)
    
t1.pencolor("black")
t1.penup()
t1.goto(-150,150)
t1.pendown()
square()

t1.penup()
t1.goto(-20,20)
t1.pendown()
square()

#for first joint 
t1.goto(-150,150)

#for second Joint
t1.penup()
t1.goto(150,150)
t1.pendown()
t1.goto(280,20)

#for third joint
t1.penup()
t1.goto(150,-150)
t1.pendown()
t1.goto(280,-280)

#for forth joint
t1.penup()
t1.goto(-150,-150)
t1.pendown()

t2=turtle.Turtle()
t2.speed(100)
t1.speed(100)
n=10
h=0
for k in range(1000):
    c= colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n
    t1.fillcolor(c)
    t1.goto(-20,-280)
    t1.begin_fill()
    t1.goto(-20,20)
    square()
    t1.end_fill()
    c= colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n
    t1.fillcolor(c)
    t1.begin_fill()
    t1.forward(300)
    t1.goto(150,150)
    t1.backward(300)
    t1.end_fill()
    
    c= colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n
    t1.fillcolor(c)
    t1.begin_fill()
    t1.right(90)
    t1.forward(300)
    t1.goto(-20,-280)
    t1.backward(300)
    t1.penup()
    t1.goto(-150,150)
    t1.pendown()
    t1.goto(-20,20)
    t1.end_fill()
    t1.left(90)


    


turtle.done()



