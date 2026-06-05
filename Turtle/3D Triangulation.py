import turtle
import random
import math
import numpy as np
try:
    from scipy.spatial import SphericalVoronoi, Delaunay
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return f"Point3D({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"

class Triangulation3D:
    def __init__(self):
        self.points = []
        self.tetrahedra = []
        self.rotation_x = 0
        self.rotation_y = 0
        self.rotation_z = 0
        
    def add_point(self, x, y, z):
        self.points.append(Point3D(x, y, z))
    
    def generate_random_points(self, num_points=15, radius=150):
        """Generate random 3D points within a sphere"""
        self.points = []
        for _ in range(num_points):
            # Generate points in a sphere using spherical coordinates
            theta = random.uniform(0, 2 * math.pi)  # azimuth
            phi = random.uniform(0, math.pi)        # elevation
            r = random.uniform(radius * 0.3, radius)  # radius
            
            x = r * math.sin(phi) * math.cos(theta)
            y = r * math.sin(phi) * math.sin(theta)
            z = r * math.cos(phi)
            
            self.add_point(x, y, z)
    
    def project_point(self, point, distance=500):
        """Project 3D point to 2D screen coordinates with rotation"""
        # Apply rotations
        x, y, z = point.x, point.y, point.z
        
        # Rotation around X-axis
        cos_x, sin_x = math.cos(self.rotation_x), math.sin(self.rotation_x)
        y_rot = y * cos_x - z * sin_x
        z_rot = y * sin_x + z * cos_x
        y, z = y_rot, z_rot
        
        # Rotation around Y-axis
        cos_y, sin_y = math.cos(self.rotation_y), math.sin(self.rotation_y)
        x_rot = x * cos_y + z * sin_y
        z_rot = -x * sin_y + z * cos_y
        x, z = x_rot, z_rot
        
        # Rotation around Z-axis
        cos_z, sin_z = math.cos(self.rotation_z), math.sin(self.rotation_z)
        x_rot = x * cos_z - y * sin_z
        y_rot = x * sin_z + y * cos_z
        x, y = x_rot, y_rot
        
        # Perspective projection
        if z + distance <= 0:
            z = -distance + 1  # Prevent division by zero
        
        scale = distance / (z + distance)
        screen_x = x * scale
        screen_y = y * scale
        
        return screen_x, screen_y, z
    
    def create_simple_tetrahedralization(self):
        """Create a simple 3D triangulation by connecting nearby points"""
        if len(self.points) < 4:
            return
        
        self.tetrahedra = []
        
        # Simple approach: for each point, find 3 nearest neighbors to form tetrahedra
        for i, point in enumerate(self.points):
            distances = []
            for j, other_point in enumerate(self.points):
                if i != j:
                    dist = math.sqrt(
                        (point.x - other_point.x)**2 +
                        (point.y - other_point.y)**2 +
                        (point.z - other_point.z)**2
                    )
                    distances.append((dist, j))
            
            distances.sort()
            
            # Take the 3 nearest points to form tetrahedra
            if len(distances) >= 3:
                # Create tetrahedron with 3 nearest neighbors
                nearest = [distances[k][1] for k in range(3)]
                tetrahedron = [i] + nearest
                
                # Avoid duplicate tetrahedra
                tetrahedron.sort()
                if tetrahedron not in self.tetrahedra:
                    self.tetrahedra.append(tetrahedron)
    
    def create_delaunay_tetrahedralization(self):
        """Create proper 3D Delaunay triangulation using scipy"""
        if not SCIPY_AVAILABLE or len(self.points) < 4:
            self.create_simple_tetrahedralization()
            return
        
        # Convert points to numpy array
        points_array = np.array([[p.x, p.y, p.z] for p in self.points])
        
        try:
            # Create 3D Delaunay triangulation
            tri = Delaunay(points_array)
            self.tetrahedra = tri.simplices.tolist()
        except:
            # Fallback to simple method
            self.create_simple_tetrahedralization()

def setup_screen():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("3D Delaunay Triangulation")
    screen.setup(800, 600)
    screen.setworldcoordinates(-400, -300, 400, 300)
    return screen

def draw_tetrahedron(t, tri, tetrahedron, line_color="cyan", point_color="yellow"):
    """Draw a single tetrahedron (4 triangular faces)"""
    indices = tetrahedron
    if len(indices) < 4:
        return
    
    points_3d = [tri.points[i] for i in indices]
    projected_points = []
    
    # Project all points
    for point in points_3d:
        proj_x, proj_y, depth = tri.project_point(point)
        projected_points.append((proj_x, proj_y, depth))
    
    # Sort by average depth for proper rendering order
    avg_depth = sum(p[2] for p in projected_points) / 4
    
    # Draw the 4 triangular faces of the tetrahedron
    faces = [
        [0, 1, 2],  # Face 1
        [0, 1, 3],  # Face 2
        [0, 2, 3],  # Face 3
        [1, 2, 3]   # Face 4
    ]
    
    t.width(1)
    
    for face in faces:
        # Calculate face normal for backface culling (simplified)
        p1, p2, p3 = [projected_points[face[i]] for i in range(3)]
        
        # Draw the triangular face
        t.penup()
        t.goto(p1[0], p1[1])
        t.pendown()
        t.color(line_color)
        
        t.goto(p2[0], p2[1])
        t.goto(p3[0], p3[1])
        t.goto(p1[0], p1[1])

def draw_points(t, tri, color="red", size=3):
    """Draw all 3D points projected to 2D"""
    for point in tri.points:
        proj_x, proj_y, depth = tri.project_point(point)
        
        # Size based on depth (closer = larger)
        point_size = max(2, size + depth / 100)
        
        t.penup()
        t.goto(proj_x, proj_y)
        t.pendown()
        t.color(color)
        t.begin_fill()
        t.circle(point_size)
        t.end_fill()

def animate_rotation(tri, screen, num_frames=200):
    """Animate the 3D triangulation with rotation"""
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    
    rotation_step = 2 * math.pi / num_frames
    
    for frame in range(num_frames):
        t.clear()
        
        # Update rotation
        tri.rotation_y += rotation_step
        tri.rotation_x += rotation_step * 0.5
        
        # Draw tetrahedra (wireframe)
        for tetrahedron in tri.tetrahedra:
            draw_tetrahedron(t, tri, tetrahedron, "lightblue")
        
        # Draw points
        draw_points(t, tri, "yellow", 3)
        
        # Add info
        t.penup()
        t.goto(0, 250)
        t.color("white")
        t.write("3D Delaunay Triangulation (Rotating)", 
                align="center", font=("Arial", 16, "bold"))
        
        t.goto(0, -280)
        t.write(f"Points: {len(tri.points)}, Tetrahedra: {len(tri.tetrahedra)}", 
                align="center", font=("Arial", 12, "normal"))
        
        screen.update()
        
        # Add a small delay
        if frame % 5 == 0:  # Update every 5 frames for smoother animation
            turtle.ontimer(lambda: None, 50)

def draw_static_3d_triangulation():
    """Draw a static 3D triangulation"""
    screen = setup_screen()
    screen.tracer(0)  # Turn off animation for faster drawing
    
    # Create triangulation
    tri = Triangulation3D()
    tri.generate_random_points(20, 120)
    
    # Set initial rotation for better view
    tri.rotation_x = math.pi / 6
    tri.rotation_y = math.pi / 4
    
    # Create tetrahedralization
    if SCIPY_AVAILABLE:
        tri.create_delaunay_tetrahedralization()
    else:
        tri.create_simple_tetrahedralization()
    
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    
    # Draw tetrahedra
    for tetrahedron in tri.tetrahedra:
        draw_tetrahedron(t, tri, tetrahedron, "cyan")
    
    # Draw points
    draw_points(t, tri, "red", 4)
    
    # Add title and info
    t.penup()
    t.goto(0, 250)
    t.color("white")
    method = "Delaunay" if SCIPY_AVAILABLE else "Simple"
    t.write(f"3D {method} Triangulation", 
            align="center", font=("Arial", 16, "bold"))
    
    t.goto(0, -280)
    t.write(f"Points: {len(tri.points)}, Tetrahedra: {len(tri.tetrahedra)}", 
            align="center", font=("Arial", 12, "normal"))
    
    t.goto(0, -260)
    t.write("Press 'r' for rotating animation", 
            align="center", font=("Arial", 10, "normal"))
    
    screen.update()
    
    # Add keyboard control for rotation
    def start_rotation():
        animate_rotation(tri, screen)
    
    screen.onkey(start_rotation, 'r')
    screen.listen()
    
    screen.exitonclick()
    return tri

if __name__ == "__main__":
    if SCIPY_AVAILABLE:
        print("Using SciPy for proper 3D Delaunay triangulation")
    else:
        print("SciPy not available, using simple 3D triangulation")
    
    print("Controls:")
    print("- Click to exit")
    print("- Press 'r' for rotating animation")
    
    draw_static_3d_triangulation()
    #turtle.done()