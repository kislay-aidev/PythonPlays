import turtle

t = turtle.Turtle()
t.screen.bgcolor("black")
t.color("white")
t.begin_fill()
t.fillcolor("red")
t.speed(10)

t.pensize(2)
#t.shape("turtle")

t.left(160)
t.forward(190)
t.circle(-95, 205.5)
t.left(130)
t.circle(-95,205.5)
t.forward(190)
t.end_fill()

t.hideturtle()

turtle.done()