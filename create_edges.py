from clustering import *
# A Python program to print all 
# combinations of given length
from itertools import combinations
import numpy as np
from csv_helper import CSVHelper

# matrix = createMatrix()
# result = DBSCAN(matrix, 0.6, 10)

result = CSVHelper.load_csv("k8_results.csv")

# noise_list = CSVHelper.load_csv("noise.csv")
# noise_list = list(map(lambda x: int(x), noise_list)) 
def get_edges(result):
    edges = []
    for c in result:
        c = [int(item) for item in c if (item != ',' and item != ' ')]
        comb = combinations(c, 2)
        # Print the obtained combinations
        for i in list(comb):
            edges.append(i)
    return edges
edges = get_edges(result)

np.savetxt("edges_k8.csv", edges, fmt='%i',delimiter=",")

