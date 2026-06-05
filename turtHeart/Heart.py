import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
pen = turtle.Turtle()
pen.color("red")
pen.pensize(3)
pen.speed(2)

# Draw the heart shape
pen.begin_fill()

pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.left(120)
pen.circle(-90, 200)
pen.forward(180)

pen.end_fill()
pen.hideturtle()

# Keep the window open until clicked
screen.exitonclick()