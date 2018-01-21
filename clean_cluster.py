import numpy as np
from csv_helper import CSVHelper

noise_list = CSVHelper.load_csv("noise.csv")
noise_list = list(map(lambda x: int(x), noise_list)) 
list_clasification = CSVHelper.load_csv("k8.csv")
list_clasification = list(map(lambda x: int(float(x)), list_clasification))    
centroids = set(list_clasification)
clusters = []

for c in centroids:
    elements = [str(i)  for i, x in enumerate(list_clasification) if (x == c and i not in noise_list)]
    # elements = [x for x in elements if x not in noise_list]
    if elements:
        clusters.append(elements)


import csv

with open("k8_results.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(clusters)
# clusters = np.asarray(clusters, dtype=int)

#np.savetxt("k8_results.csv", clusters, fmt='%i',delimiter=",")

#print(clusters)
# print(centroids)
# print(noise_list)