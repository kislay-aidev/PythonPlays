import turtle
import math

t = turtle.Turtle()
t.screen.bgcolor("black")
t.pencolor("red")
t.speed(0)
t.hideturtle()

c = 0
d = 0

while True:
    # Draw a hollow pot (rotating squares)
    for i in range(4):
        t.forward(80)
        t.right(90)
    t.right(5)
    c += 1
    
    if c >= 360 / 5:  # One pot completed
        # Radial offset: move outward and rotate
        t.penup()
        angle = d * 30
        rad = math.radians(angle)
        x = 100 * math.cos(rad)
        y = 100 * math.sin(rad)
        t.goto(x, y)
        t.setheading(angle)
        t.pendown()

        c = 0
        d += 1
        
        if d >= 12:  # Number of pots
            break

turtle.done()