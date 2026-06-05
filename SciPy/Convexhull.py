import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

points = np.random.rand(30, 2)  # 30 random 2D points

hull = ConvexHull(points)

plt.plot(points[:, 0], points[:, 1], 'o')  # plot all points

# draw edges of the hull
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')

# highlight the hull vertices
plt.plot(points[hull.vertices, 0], points[hull.vertices, 1], 'r--', lw=2)
plt.plot(points[hull.vertices[0], 0], points[hull.vertices[0], 1], 'ro')  # start point
plt.title("Convex Hull using SciPy")
plt.show()