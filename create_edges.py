from clustering import *

edges = []
matrix = createMatrix()
result = DBSCAN(matrix, 0.6, 10)

for c in result:
    for n in c:
        

