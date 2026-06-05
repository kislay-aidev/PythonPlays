import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

a = np.array([[2, 4], [3, 4], [3, 0], [2, 2], [4, 1], [1, 2], [5, 0], [3, 1], [1, 2], [0, 2]])

hull = ConvexHull(a)
hull_points = hull.simplices

plt.scatter (a[:, 0], a[:, 1])
for i in hull_points:
    plt.plot(a[i, 0], a[i, 1], 'k-')
plt.show()