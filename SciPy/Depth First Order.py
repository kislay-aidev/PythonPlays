import numpy as np
from scipy.sparse.csgraph import depth_first_order as dfo
from scipy.sparse import csr_matrix as cm

#array building
a = np.array ([[0, 1, 0, 1], [1, 1, 1, 1], [2, 1, 1, 0], [0, 1, 0, 1]])
print(a)

b = cm(a)
print("\n",dfo(b, return_predecessors = True, i_start = 1))