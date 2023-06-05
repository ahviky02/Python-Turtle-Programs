#In this Program We are Drawing Cos(θ) Graph  
#it is Created By Ahvi..
import turtle


h=turtle.Turtle()  # h is used for Draw curve 
s=turtle.Screen()
s.bgcolor('cyan')
h.pensize(2)
h.penup()
h.goto(-112,0)
h.pendown()
h.pencolor('navy')

#It function are Used to turn turtle to right Side 
def round(a,d,r):
    for i in range(r):
        h.right(a)
        h.forward(d)
  
#It function are Used to turn turtle to left Side 
def round1(a,d,r):
    for i in range(r):
        h.left(a)
        h.forward(d)
        
        
t1=turtle.Turtle()  # t1 turtle is used For Darw X and Y Axis... 
t1.forward(700)
t1.backward(1400)
t1.penup()
t1.goto(0,0)
t1.pendown()
t1.right(90)
t1.backward(500)
t1.forward(1000)
h.left(80)


t2=turtle.Turtle() # t2 turtle is Used For Write A Value ..... 
t2.hideturtle()
t2.pensize(2)
t2.penup()
t2.goto(-300,300)
t2.pendown()
t2.write('-1<=cos(θ)<=1',font=('Arial',25,'normal'))

# It is angle name .... 
t2.penup()
t2.goto(115,0)
t2.pendown()
t2.write('π/2',font=('Arial',16,'normal'))

t2.penup()
t2.goto(230,0)
t2.pendown()
t2.write('π',font=('Arial',16,'normal'))

t2.penup()
t2.goto(345,0)
t2.pendown()
t2.write('3π/2',font=('Arial',16,'normal'))

t2.penup()
t2.goto(455,0)
t2.pendown()
t2.write('2π',font=('Arial',16,'normal'))

t2.penup()
t2.goto(565,0)
t2.pendown()
t2.write('5π/2',font=('Arial',16,'normal'))

t2.penup()
t2.goto(675,0)
t2.pendown()
t2.write('3π',font=('Arial',16,'normal'))



t2.penup()
t2.goto(-115,0)
t2.pendown()
t2.write('π/2',font=('Arial',16,'normal'))

t2.penup()
t2.goto(-230,0)
t2.pendown()
t2.write('π',font=('Arial',16,'normal'))

t2.penup()
t2.goto(-345,0)
t2.pendown()
t2.write('3π/2',font=('Arial',16,'normal'))

t2.penup()
t2.goto(-455,0)
t2.pendown()
t2.write('2π',font=('Arial',16,'normal'))

t2.penup()
t2.goto(-565,0)
t2.pendown()
t2.write('5π/2',font=('Arial',16,'normal'))

t2.penup()
t2.goto(-675,0)
t2.pendown()
t2.write('3π',font=('Arial',16,'normal'))

#and it is Range
t2.penup()
t2.goto(0,110)
t2.pendown()
t2.write(' 1',font=('Arial',16,'normal'))

t2.penup()
t2.goto(0,-115)
t2.pendown()
t2.write(' -1',font=('Arial',16,'normal'))


#it used to Draw Y Axis Right side Curve
for i in range(2):
    #it used to Draw Upper Curve
    round(1,3,60)
    round(4,0.7,10)
    round(1,3,60)
    
    #it used to Draw Lower Curve
    round1(1,3,60)
    round1(4,0.7,10)
    round1(1,3,60)

h.penup()
h.goto(-112,0)
h.pendown()
h.left(180)

#it used to Draw Y Axis Left side Curve
for i in range(2):
    #it used to Draw Y Axis Right side Curve
    round(1,3,60)
    round(4,0.7,10)
    round(1,3,60)
    
    #it used to Draw Lower Curve
    round1(1,3,60)
    round1(4,0.7,10)
    round1(1,3,60)
    
turtle.done()   







