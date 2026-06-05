import turtle
import random
import math
from scipy.spatial import Delaunay
import numpy as np

def setup_screen():
    """Set up the turtle graphics screen"""
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Delaunay Triangulation")
    screen.setup(800, 600)
    screen.setworldcoordinates(-400, -300, 400, 300)
    return screen

def generate_random_points(num_points=20, width=700, height=500):
    """Generate random points within the screen bounds"""
    points = []
    for _ in range(num_points):
        x = random.uniform(-width/2, width/2)
        y = random.uniform(-height/2, height/2)
        points.append([x, y])
    return np.array(points)

def draw_point(t, x, y, color="red", size=5):
    """Draw a point at given coordinates"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(size)
    t.end_fill()

def draw_triangle(t, p1, p2, p3, line_color="blue", line_width=1):
    """Draw a triangle given three points"""
    t.penup()
    t.goto(p1[0], p1[1])
    t.pendown()
    t.color(line_color)
    t.width(line_width)
    
    # Draw the triangle
    t.goto(p2[0], p2[1])
    t.goto(p3[0], p3[1])
    t.goto(p1[0], p1[1])

def draw_delaunay_triangulation():
    """Main function to create and draw Delaunay triangulation"""
    # Set up screen and turtle
    screen = setup_screen()
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    
    # Generate random points
    points = generate_random_points(25)
    
    # Create Delaunay triangulation
    tri = Delaunay(points)
    
    # Draw triangles
    print("Drawing triangles...")
    for simplex in tri.simplices:
        p1 = points[simplex[0]]
        p2 = points[simplex[1]]
        p3 = points[simplex[2]]
        draw_triangle(t, p1, p2, p3, "lightblue", 1)
    
    # Draw points on top of triangles
    print("Drawing points...")
    for point in points:
        draw_point(t, point[0], point[1], "red", 3)
    
    # Add title
    t.penup()
    t.goto(0, 250)
    t.color("black")
    t.write("Delaunay Triangulation", align="center", 
            font=("Arial", 16, "bold"))
    
    # Add info
    t.goto(0, -280)
    t.write(f"Points: {len(points)}, Triangles: {len(tri.simplices)}", 
            align="center", font=("Arial", 12, "normal"))
    
    t.hideturtle()
    print(f"Generated {len(points)} points and {len(tri.simplices)} triangles")
    
    # Keep window open
    screen.exitonclick()
    return tri, points

# Alternative version without scipy (basic triangulation)
def distance(p1, p2):
    """Calculate distance between two points"""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def draw_simple_triangulation():
    """Simple triangulation without scipy - connects nearest neighbors"""
    screen = setup_screen()
    t = turtle.Turtle()
    t.speed(0)
    
    # Generate points
    points = []
    for _ in range(15):
        x = random.uniform(-300, 300)
        y = random.uniform(-200, 200)
        points.append([x, y])
    
    # Simple triangulation - connect each point to its two nearest neighbors
    triangles = []
    for i, point in enumerate(points):
        distances = []
        for j, other_point in enumerate(points):
            if i != j:
                dist = distance(point, other_point)
                distances.append((dist, j))
        
        distances.sort()
        # Connect to two nearest neighbors
        if len(distances) >= 2:
            nearest1 = distances[0][1]
            nearest2 = distances[1][1]
            # Create triangle with next nearest point
            if len(distances) >= 3:
                nearest3 = distances[2][1]
                triangles.append([i, nearest1, nearest3])
    
    # Draw triangles
    for triangle in triangles:
        p1 = points[triangle[0]]
        p2 = points[triangle[1]]
        p3 = points[triangle[2]]
        draw_triangle(t, p1, p2, p3, "lightgreen", 1)
    
    # Draw points
    for point in points:
        draw_point(t, point[0], point[1], "blue", 3)
    
    t.penup()
    t.goto(0, 250)
    t.color("black")
    t.write("Simple Triangulation", align="center", 
            font=("Arial", 16, "bold"))
    
    t.hideturtle()
    screen.exitonclick()

if __name__ == "__main__":
    try:
        # Try with scipy for proper Delaunay triangulation
        draw_delaunay_triangulation()
    except ImportError:
        print("SciPy not available, using simple triangulation...")
        draw_simple_triangulation()