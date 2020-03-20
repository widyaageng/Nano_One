import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([10, 9, 8])
C = np.reshape(np.matmul(A, B), (2,1))
print(np.shape(A))
print(np.shape(B))
print(np.shape(C))
print(C)