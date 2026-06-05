import turtle

b = turtle.Turtle()
b.speed(3)

b.color("blue", "cyan")

b.begin_fill()
for i in range (6):
    b.forward(100)
    b.left(90)

b.penup()
b.right(90)
b.forward(50)
b.pendown()

for i in range (4):
    b.forward(100)
    b.left(90)

b.hideturtle()
b.end_fill()

turtle.done()