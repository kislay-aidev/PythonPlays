import turtle

# Create a turtle object and set speed
t = turtle.Turtle()
t.speed(0) # Fastest speed

# Define colors
colors = ["red", "purple", "blue", "green", "orange", "yellow"]

# Draw a colorful spiral
for x in range(360):
    t.pencolor(colors[x % 6]) # Cycle through colors
    t.width(x / 100 + 1)      # Increase pen width gradually
    t.forward(x)              # Move forward, increasing distance
    t.left(59)                # Turn left

# Keep the window open
turtle.done()