import numpy as np

a1 = np.array([[0, 1, 0], [1, 0, 1]])
a1 = np.zeros((3, 3, 2, 2))
a2 = np.array([1, 0])
a3 = np.array([[1], [0]])
a4 = np.array([[1], [1]])

print(np.logical_xor(a1, a2))
# print(np.logical_xor(a1, a3))
# print(np.logical_xor(a1, a4))
