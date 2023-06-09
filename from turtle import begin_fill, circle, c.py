from turtle import begin_fill, circle, color, colormode, distance, down, end_fill, fd, hideturtle, left, pensize, right, seth, up
import turtle


colormode(255)
red =(223,35,35)
green=(75,183,75)
yellow=(252,216,9)
blue=(86,146,195)
pensize(4)

r=120
seth(-150)
up()

color(red)
begin_fill()
fd(r)
down()
right(90)
circle(-r,120)
fd(r*3**.5) 
left(120)
circle(2*r,120)
left(60)
fd(r*3**.5)
end_fill()


left(180)
color(green)
begin_fill()
fd(r*3**.5)
left(120)
circle(2*r,120)
left(60)
fd(r*3**.5)
left(180)
circle(-r,120)
end_fill()

 
left(180)
circle(r,120)
color(yellow)
begin_fill()
circle(r,120)
right(180)
fd(r*3**.5)
right(60)
circle(-2*r,120)
right(120)
fd(r*3**.5)

end_fill()

pensize(0)
up()
left(98)
fd(r/20)
seth(60)
color(blue)
down()
begin_fill()
circle(distance(0,0))
end_fill()
hideturtle()
turtle.done()




