import turtle
import colorsys

# Setup screen
t = turtle.Turtle()
t.screen.bgcolor("black")
t.speed(0)
t.hideturtle()  # Hide the turtle for speed and beauty

# Color settings
n = 36  # Number of pots
colors = [colorsys.hsv_to_rgb(i/n, 1, 1) for i in range(n)]  # Generate rainbow colors

c = 0
d = 0

while True:
    # Set color dynamically
    r, g, b = colors[d % n]
    t.pencolor(r, g, b)
    
    # Draw a tilted hollow pot (rotating squares)
    for i in range(4):
        t.forward(80)
        t.right(90)
    t.right(10)  # Smaller step for more rotation beauty
    c += 1
    
    if c >= 36:  # One pot complete (36 steps of 10°)
        t.penup()
        t.forward(150)  # Move away for next pot
        t.right(30)     # Tilt next pot
        t.pendown()
        c = 0
        d += 1
        
        if d >= n:  # Stop after n pots
            break

turtle.done()
