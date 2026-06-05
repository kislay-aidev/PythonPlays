import turtle

t = turtle.Turtle()
t.screen.bgcolor("black")
t.color("white")
t.begin_fill()
t.fillcolor("red")
t.speed(10)

t.pensize(3)
t.shape("turtle")

t.left(160)
t.forward(190)
t.circle(-95, 205.5)
t.left(130)
t.circle(-95,205.5)
t.forward(190)
t.end_fill()
t.left(120.5)
t.forward(350)

t.write("I Love You", True, align = "right")
#t.hideturtle()
turtle.exitonclick()