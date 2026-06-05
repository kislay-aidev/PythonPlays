import numpy as np
from scipy.sparse import csr_matrix

# Create initial CSR matrix
data = [1, 1, 1]       # Values
indices = [1, 1, 2]    # Column indices
indptr = [0, 2, 3]     # Row pointers (CSR format)
shape = (2, 3)         # Matrix shape

# Create CSR matrix with duplicates
csr_mat = csr_matrix((data, indices, indptr), shape=shape)
print("Before sum_duplicates():")
print(csr_mat)

# Sum duplicates
csr_mat.sum_duplicates()
print("\nAfter sum_duplicates():")
print(csr_mat)