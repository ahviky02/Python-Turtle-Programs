import turtle


h=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('darkgray')
h.pensize(2)
h.penup()
h.goto(-100,100)
h.pendown()
def round(a,d,r):
    for i in range(r):
        h.right(a)
        h.forward(d)
        
def round1(a,d,r):
    for i in range(r):
        h.left(a)
        h.forward(d)

    

h.forward(70)
h.left(60)
round(3,2,17)
h.left(81)
h.forward(15)
h.left(90)
h.forward(20)
h.right(90)
h.forward(7)
h.right(90)
h.forward(48)
h.right(90)
h.forward(7)
h.right(90)
h.forward(20)
h.left(90)
h.forward(15)
h.left(87)


round(3,2,17)
h.left(54)
h.forward(70)

round(10,3,9)
h.forward(55)
h.right(140)
round1(5,2,20)
h.left(80)
round1(5,2,20)
h.right(177)
round(5,2,20)
h.hideturtle()


h.right(42)
h.forward(30)
round1(10,2,9)
h.forward(34)
h.left(60)


round(3,2,38)

h.left(54)
h.forward((70))


#water 
t2=turtle.Turtle()
t2.speed(100)
t2.hideturtle()
def move():
    t2.fillcolor('cyan')
    t2.begin_fill()
    t2.circle(10)
    t2.end_fill()
    t2.clear()

t3=turtle.Turtle()
t3.speed(100)
t3.hideturtle()
def move2():
    t3.fillcolor('cyan')
    t3.begin_fill()
    t3.circle(10)
    t3.end_fill()
    t3.clear()  

while True:
    t2.penup()
    t2.goto(100,-10)
    t2.pendown()
    move()
    
    t3.penup()
    t3.goto(100,-80)
    t3.pendown()
    move2()
    
    t2.penup()
    t2.goto(100,-30)
    t2.pendown()
    move()
    
    t3.penup()
    t3.goto(100,-105)
    t3.pendown()
    move2()
    
    t2.penup()
    t2.goto(100,-60)
    t2.pendown()
    move()
    
    t3.penup()
    t3.goto(100,-20)
    t3.pendown()
    move2()
    
    t2.penup()
    t2.goto(100,-90)
    t2.pendown()
    move()
    
    t3.penup()
    t3.goto(100,-10)
    t3.pendown()
    move2()
    
    t2.penup()
    t2.goto(100,-120)
    t2.pendown()
    move()
    
    t3.penup()
    t3.goto(100,-60)
    t3.pendown()
    move2()
    
    t2.penup()
    t2.goto(100,-150)
    t2.pendown()
    move()
    
    t3.penup()
    t3.goto(100,-35)
    t3.pendown()
    move2()
    
    t2.penup()
    t2.goto(100,-70)
    t2.pendown()
    move()
    
    
    
    

