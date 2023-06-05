#Rose program create by Ahvi
import colorsys
import turtle


t=turtle.Turtle()
s= turtle.Screen()
t.pensize(2)
t.fillcolor('deeppink')
t.begin_fill()
def rr(a,d,r):
   for i in range(r):
         t.left(a)
         t.forward(d)

def rl(a,d,r):
       for i in range(r):
              t.right(a)
              t.forward(d)
              
def rr1(a,d,r):
       for i in range(r):
         t1.left(a)
         t1.forward(d)

def rl1(a,d,r):
       for i in range(r):
              t1.right(a)
              t1.forward(d)


rr(0.5,2,15)  
rr(1,1,30)  
rr(5,3,10) 
rr(1.2,3,15)
rl(1,3,19)
rl(2,2,7)
rl(1,2,5)
rr(3,3,7)
rr(5,2,10)
rr(6,3,6)
rr(1.5,1.5,10)
rr(3,1.7,15)

t.right(120)
rr(5,3,25)

t.right(120)
rr(4,2,8)
rr(4,3,8)
rr(4,2,15)
rr(6,3,5)
rr(2.2,4,10)
t.right(5)
rl(2,3.3,12)
rl(1,2,10)
rl(2,2.7,5)

t.left(13)
rr(5,6,3)
rr(4,5,7)
t.left(25)
rr(2,4,10)
rr(0.2,5,5)
t.left(5)
t.forward(4)
t.end_fill()



#branch

#leaf 1
t.fillcolor('lime')
t.begin_fill()
t.left(170)
rr(4,5,10)
rr(3,5,9)
rr(5,3,6)
rl(2,4,6)

t.right(250)
rr(2,4,35)
t.end_fill()

t.left(150)
rl(2,5,13)
rr(4,4,13)


#cre
t.left(190)
t.penup()
t.goto(0,0)
t.pendown()
rr(1.2,3,15)
rl(1,3,19)
rl(2,2,7)
rl(1,2,5)
rr(3,3,7)
rr(5,2,10)
rr(6,3,6)
rr(1.5,1.5,10)
rr(3,1.7,15)

t.right(60)
rl(3,4,5)
rr(5,2,20)
t.hideturtle()





#leaf 2

t1=turtle.Turtle()
t1.pensize(2)
t1.fillcolor('lime')
t1.begin_fill()
rl1(2,3,16)
rl1(2,4,10)
rl1(1,3,12)
t1.right(100)
rl1(4,4,11)
rl1(4,5,5)
rl1(0,5,8)
t1.forward(10)

t1.right(110)
rl1(4,3,7)
t1.right(18)
rl1(2,5,15)
t1.end_fill()

t2= turtle.Turtle()
t2.goto(-8,0)
t2.pensize(20)
t2.pencolor('green')
t2.right(88)
for i in range(20):
       t2.right(1)
       t2.forward(5)
for i in range(20):
       t2.right(3)
       t2.forward(6)






turtle.done()
    









