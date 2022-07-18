# https://www.wolframalpha.com/input?i2d=true&i=%7B%7B0%2C1%2C0%2C1%2C1%2C1%7D%2C%7B1%2C0%2C1%2C0%2C1%2C1%7D%2C%7B0%2C1%2C0%2C1%2C1%2C1%7D%2C%7B1%2C0%2C1%2C0%2C1%2C1%7D%2C%7B1%2C1%2C1%2C1%2C0%2C0%7D%2C%7B1%2C1%2C1%2C1%2C0%2C0%7D%7D

import numpy as np
from numpy.linalg import inv

S = [[-1, -1, 0, 0, -1, 1], [0, 1, 0, -1, 0, 1], [-1, -1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1], [1, 0, -1, 0, 0, 1], [1, 0, 1, 0, 0, 1]]
J = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]]
Sinv = inv(S)

print(np.matmul(np.matmul(np.matmul(S, J), Sinv), [1, 2, 3, 4, 5, 6]))
