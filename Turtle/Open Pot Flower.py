#open pot flower
import turtle

t = turtle.Turtle()

t.screen.bgcolor("black")
t.pencolor("red")
t.speed(0)

c = 0
d = 0

while True:
    for i in range(4):
        t.forward(80)
        t.right(90)
    t.right(5)
    c += 1
    if c >= 360/5:
        t.forward(50)
        c = 0
        d += 1
        if d >= 12:
            break
        
turtle.done()