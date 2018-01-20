from clustering import *
import pylab
import matplotlib.pyplot as plt 



epsilonValues= [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
nminValues= [5, 10, 20, 30, 50, 80, 100, 200, 300, 500] 
matrix = createMatrix()

results = []
simplified = []
for i in range(len(epsilonValues)):
    values = DBSCAN(matrix, epsilonValues[i], nminValues[i])
    results.append(values)
    simplified.append(values['clusters'])

pylab.figure()
pylab.plot(simplified,'bo', simplified,':k')
pylab.title('Number of clusters for fixed epsilon (e = 0.5) and incremental minimun nodes' )
pylab.xlabel('Combinations')
pylab.ylabel('Number of Clusters ')

for i in range(len(epsilonValues)):
    txt = '(e:' + str(epsilonValues[i]) + ', n:' + str(nminValues[i]) + ')'
    pylab.annotate(txt, (i,simplified[i]))

pylab.show()