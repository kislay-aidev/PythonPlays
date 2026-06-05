import turtle

ckrit = turtle.Turtle()
ckrit.speed(0)

ckrit.screen.bgcolor("black")
ckrit.pencolor("cyan")

a = 0
b = 0
ckrit.penup()
ckrit.goto(0,0)
ckrit.pendown()

while True:
    ckrit.forward(a)
    ckrit.right(b)
    a+= 3
    b+= 1
    if b == 210:
        break
    ckrit.hideturtle()

turtle.done()