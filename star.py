import turtle


t=turtle.Turtle()
s=turtle.Screen()
t.speed(10)

s.bgcolor("black")

col=("yellow","blue","white","red","lime")

c=0
 
for i in range(100):
     t.forward(i*10)
     t.right(144)
     t.color(col[c])
     if c==4:
         c=0
     else:
         c+=1

   
   
  