import numpy as np
from scipy.sparse.csgraph import bellman_ford as bf
from scipy.sparse import csr_matrix as cm

#array building
a = np.array ([[0, -1, 2], [1, 0, 0], [2, 0, 0]])
b = cm(a)
print(bf(b, return_predecessors = True, indices = 1))