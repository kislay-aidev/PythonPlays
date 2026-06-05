import turtle
import math

b = turtle.Turtle()
b.color("red", "yellow")
b.speed(100000)

for i in range(400):
    b.forward(15.3)    
    b.left(math.cos(i/10.4)*25.6)    
    b.left(20.7    )
    
turtle.done()