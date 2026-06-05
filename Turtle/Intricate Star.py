import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Black background to make the star stand out
screen.title("Red and Yellow Star Pattern")

# Create a turtle
star = turtle.Turtle()
star.speed(0)  # Medium speed for nice animation

# Set colors
star.color("red", "pink")  # Red outline, yellow fill
#star.pensize(3)  # Thicker lines for better visibility

# Position the turtle
star.penup()
star.goto(0, -50)  # Start from bottom center
star.pendown()

# Draw the star
star.begin_fill()
while True:
    star.forward(500)
    star.right(169)  # 144 degrees for a 5-pointed star
    if star.heading() < 2:
        break
star.end_fill()

# Hide the turtle and keep window open
#star.hideturtle()
screen.mainloop()  # Click to close