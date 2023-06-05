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


turtle.penup()
turtle.goto(-200,-190)
turtle.pendown()
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


turtle.penup()
turtle.goto(200,-190)
turtle.pendown()
turtle.pencolor("cyan")
turtle.bgcolor("black")
turtle.speed(100)

turtle.left(45)
for k in range(4):
    for i in range(45):
        turtle.circle(i/2)
        turtle.forward(2)

    for i in range(45):
        turtle.circle((45-i)/2)
        turtle.forward(2)
    turtle.left(90)
    
turtle.hideturtle()






turtle.done()