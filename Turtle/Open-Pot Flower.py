import turtle

t = turtle.Turtle()
t.screen.bgcolor("black")
t.pencolor("red")
t.speed(0)

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
        t.penup()
        t.forward(100)  # Move away (parallel shift)
        t.right(30)     # Tilt the next pot
        t.pendown()
        c = 0
        d += 1
        
        if d >= 12:  # Number of pots
            break

turtle.done()
