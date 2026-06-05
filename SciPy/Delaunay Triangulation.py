import numpy as np
from scipy.spatial import Delaunay as dl
import matplotlib.pyplot as plt

a = np.array([[2,4], [3,4], [3,0], [2,2], [4,1]])
b = dl(a).simplices

#plotting graph
plt.triplot(a[:, 0], a[:, 1], b, color = 'black')
plt.scatter(a[:, 0], a[:, 1], color = 'red')
plt.show()