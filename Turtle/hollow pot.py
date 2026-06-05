import turtle

t = turtle.Turtle()

t.screen.bgcolor("black")
t.pencolor("red")
t.speed(0)

while True:
    for i in range(4):
        t.forward(80)
        t.right(90)
    t.right(5)
    if t.heading() < 1:
        break
        
turtle.done()