from clustering import *
# A Python program to print all 
# combinations of given length
from itertools import combinations
import numpy as np
from csv_helper import CSVHelper

matrix = createMatrix()
results = DBSCAN(matrix, 0.5, 12)

# result = CSVHelper.load_csv("k2.csv")
# result = list(map(lambda x: int(float(x)), result)) 
# noise_list = CSVHelper.load_csv("noise.csv")
# noise_list = list(map(lambda x: int(x), noise_list)) 
def get_edges(result):
    edges = []
    for c in result:
        # c = [int(item) for item in c if (item != ',' and item != ' ')]
        comb = combinations(c, 2)
        # Print the obtained combinations
        for i in list(comb):
            edges.append(i)
    return edges
edges = get_edges(results)

np.savetxt("edges_2.csv", edges, fmt='%i',delimiter=",")

