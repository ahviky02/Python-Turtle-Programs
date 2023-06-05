import turtle


turtle.Turtle()
turtle.Screen()
turtle.pencolor("cyan")
turtle.bgcolor("black")
turtle.speed(100)

turtle.left(45)
for k in range(5):
    for i in range(36):
        turtle.circle(i/2)
        turtle.forward(2)

    for i in range(36):
        turtle.circle((36-i)/2)
        turtle.forward(2)
    turtle.left(72)

turtle.hideturtle()




turtle.done()