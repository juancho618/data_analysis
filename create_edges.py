from clustering import *
# A Python program to print all 
# combinations of given length
from itertools import combinations
import numpy as np

edges = []
matrix = createMatrix()
result = DBSCAN(matrix, 0.6, 10)

for c in result:
    # Get all combinations of [1, 2, 3]
    # and length 2
    comb = combinations(c, 2)
    # Print the obtained combinations
    for i in list(comb):
        edges.append(i)

np.savetxt("edges.csv", edges, fmt='%i',delimiter=",")

