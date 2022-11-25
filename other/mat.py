import numpy as np

M = np.array([[.9, .4], [.1, .6]])
N = np.array([[1], [0]])

for i in range(1000):
    N = M@N
print(N)