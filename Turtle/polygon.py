import turtle
import random

t = turtle.Turtle()
t.speed(0)

colors = ["red", "blue", "pink", "brown", "orange", "green", "gray", "alice blue", "aquamarine", "burlywood", "chocolate1", "beige", "blanched almond"]

random.shuffle(colors)

for i in range (3,9):
    angle = 360/i
    t.pencolor(colors [i - 3])
    for p in range (i):
        t.forward(100)
        t.right(angle)

t.screen.exitonclick()