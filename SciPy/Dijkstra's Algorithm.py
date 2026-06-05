import turtle

# Setup
t = turtle.Turtle()
t.speed(0)
positions = {
    'A': (-200, 0), 'B': (-100, 100), 'C': (-100, -100),
    'D': (0, 100), 'E': (0, -100), 'F': (100, -100)
}
edges = [
    ('A', 'B', 4), ('A', 'C', 5),
    ('B', 'D', 9),
    ('C', 'E', 3),
    ('D', 'E', 11),
    ('E', 'F', 6)
]

# Draw nodes
for node, (x, y) in positions.items():
    t.penup()
    t.goto(x, y)
    t.dot(30, "skyblue")
    t.write(node, align="center", font=("Arial", 12, "bold"))

# Draw edges
for u, v, w in edges:
    x1, y1 = positions[u]
    x2, y2 = positions[v]
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)
    mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
    t.penup()
    t.goto(mid_x, mid_y)
    t.write(str(w), align="center", font=("Arial", 10, "normal"))

t.hideturtle()
turtle.done()