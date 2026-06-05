import numpy as np
from scipy.sparse.csgraph import dijkstra as dj
from scipy.sparse import csr_matrix as cm
a = np.array ([[0, 1, 2], [1, 0, 0], [2, 0, 0]])
b = cm(a)

print(dj(b, return_predecessors = True, indices = 0))