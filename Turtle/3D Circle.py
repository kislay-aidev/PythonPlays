import turtle
import random

t = turtle.Turtle()
t.hideturtle()  
t.speed(0)
turtle.colormode(255)

while True:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    t.pencolor((r, g, b))
    
    t.circle(100)
    t.left(5)
    if t.heading() < 2:
        break

turtle.exitonclick()