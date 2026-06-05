import turtle

b = turtle.Turtle()

b.color("blue", "cyan")

b.begin_fill()
b.forward(100)
b.left(90)
b.forward(100)
b.left(90)
b.forward(100)
b.left(90)
b.forward(100)

b.penup()
b.forward(50)
b.pendown()

b.forward(100)
b.left(90)
b.forward(100)
b.left(90)
b.forward(100)
b.left(90)
b.forward(100)
b.end_fill()

turtle.done()