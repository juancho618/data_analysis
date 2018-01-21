import numpy as np
from csv_helper import CSVHelper
from clustering import createMatrix
import pylab
from functools import reduce
import matplotlib.pyplot as plt 

matrix_distance = createMatrix()
matrix_distance = np.asarray(matrix_distance)



def get_distances(matrix, centroids, cluster):
    distances =[]
    for c in centroids: 
        members = [ i  for i, x in enumerate(cluster) if x == c]
        similarity = matrix[c][0]
        dist = list(map(lambda x: 1-x, similarity[0]))
        dist =[dist[i]**2 for i in members]
        distances.append(sum(dist))
    return(distances)

pairs = []
for i in range(11):
    ssq = 0
    
    list_clasification = CSVHelper.load_csv("k"+str(i+2)+".csv")
    list_clasification = list(map(lambda x: int(float(x)), list_clasification))    
    centroids = set(list_clasification)
    # centroids = list(map(lambda x: int(float(x)), centroids))

    distances = get_distances(matrix_distance,centroids, list_clasification)
    distances = np.asarray(distances)
    ssq = reduce(lambda x,y: x+y,distances)
    print(ssq)
    pairs.append((i+2, ssq))

pairs = np.asarray(pairs, dtype=int)
print(pairs[:,0])
pylab.figure()
pylab.plot(pairs[:,0],pairs[:,1],'bo', pairs[:,0],pairs[:,1],':k')
pylab.title('Number of clusters vs SSE distances in the clusters' )
pylab.xlabel('Number of clusters')
pylab.ylabel('SSE distance')

pylab.show()
