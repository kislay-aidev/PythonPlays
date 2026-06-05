import numpy as np
from scipy.sparse import csr_matrix as cm

a = np.array ([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
b = cm(a).tocsc()

print(b)