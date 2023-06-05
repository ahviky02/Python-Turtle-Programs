import turtle


turtle.Turtle()
turtle.Screen()
turtle.pencolor("yellow")
turtle.bgcolor("black")
turtle.speed(100)

for k in range(4):
    for i in range(45): 
        turtle.left(1)
        turtle.circle(i/2)
        turtle.forward(2)

    for i in range(45):
        turtle.left(1)
        turtle.circle((45-i)/2)
        turtle.forward(2)

turtle.hideturtle()




turtle.done()