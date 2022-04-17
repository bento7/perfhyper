from sys import path
from os import getcwd
path.append(getcwd() + "..")
print(path)
import numpy as np
mat = np.array([1,3,5])
print(mat.max())