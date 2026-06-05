import turtle

t = turtle.Turtle()
#t.speed(0)

for i in range (4):
    t.fd(100)
    t.lt(90)
    
for i in range (4):
    t.rt(90)
    t.fd(100)
    
for i in range (4):
    t.lt(90)
    t.fd(100)
    
for i in range (4):
    t.fd(100)
    t.rt(90)
    
def circle(rad,head):
    for i in range(1):
        t.circle(rad)
    t.setheading(head)
    
circle(50, 90)
circle(-50, 90)
circle(50, 0)

#t.setheading(0)
circle(-50, 0)

circle(75, 90)
circle(-75, 90)
circle(75, 0)
circle(-75, 0)

turtle.done()