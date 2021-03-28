import numpy as np

A = np.array([
  [1, -1, 1],   # x - y = 1
  [1, 1, 55]    # x + y = 55
])

A[0] += A[1]    # Add row 2 to row 1
# [[ 2  0 56]
#  [ 1  1 55]]

A[0] //= 2      # Halve row 2 because everything is even
# [[ 1  0 28]
#  [ 1  1 55]]

A[1] -= A[0]    # Subtract row 1 from row 2
# [[ 1  0 28]
#  [ 0  1 27]]
# So (x, y) = (28, 27)

A = np.array([
  [1, -1],
  [1, 1]
])

I = np.eye(2)
M = np.concatenate((A, I), axis=1)
# [[ 1. -1.  1.  0.]
#  [ 1.  1.  0.  1.]]

M[0] += M[1]      # Same 3 steps as before
M[0] /= 2         # Can't use '//' this time
M[1] -= M[0]
# [[ 1.   0.   0.5  0.5]
#  [ 0.   1.  -0.5  0.5]]

A_inv = M[:, 2:]  # Get last two columns of M
# [[ 0.5  0.5]
#  [-0.5  0.5]]

print(np.matmul(A, A_inv))
# [[1. 0.]
#  [0. 1.]]
