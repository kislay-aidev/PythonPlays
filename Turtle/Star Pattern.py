import turtle

t = turtle.Turtle()
t.speed(0)

t.color ("red")
t.fillcolor("yellow")

t.begin_fill()
while True:
    t.left(170)
    t.forward (180)
    t.circle(-90, 100)
    #t.forward(180)
    if t.heading() < 1:
        break
t.end_fill()

turtle.done()