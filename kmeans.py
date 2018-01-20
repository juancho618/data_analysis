# X: data matrix of size (n_samples,n_features)
# n_clusters: number of clusters
# output 1: labels of X with size (n_samples,)
# output 2: centroids of clusters
from euclidean_distance import euclidean_vectorized
from clustering import createMatrix
import numpy as np

matrix_distance = createMatrix()
matrix_distance = np.asarray(matrix_distance)

def get_distances(matrix, centroids):
    distances =[]
    for c in centroids: 
        similarity = matrix[c][0]
        dist = list(map(lambda x: 1-x, similarity[0]))
        distances.append(dist)
    return np.asarray(distances)
        
def assign_labels(distances, indices):
    labels = np.zeros(distances.shape[1])
    for i in range(distances.shape[1]):
        min_ind = np.argmin(distances[:,i])
        labels[i] = indices[min_ind]
    return labels

def new_centroid(matrix, members, indices):
    min_indx = -1
    min_dist = 500000000000
    for m in members:
        similarity = matrix[m][0]
        dist = list(map(lambda x: 1-x, similarity[0]))
        total_dist = sum(dist)
        if total_dist < min_dist and m not in indices:
            min_indx = m
            min_dist = total_dist
    return min_dist
        
    

def kmeans(X,n_clusters):
    # initialize labels and prev_labels. prev_labels will be compared with labels to check if the stopping condition
    # have been reached.
    prev_labels = np.zeros(X.shape[0])
    labels = np.zeros(X.shape[0])
    indices_results = []
    # init random indices
    indices = np.random.choice(X.shape[0], n_clusters, replace=False)
    indices_results.append(indices)
    # assign centroids using the indices
    # centroids = X[indices]
    
    # the interative algorithm goes here
    while (True):
        # calculate the distances to the centroids
        distances = get_distances(X, indices)
        print(labels, indices)

        # assign labels
        labels = assign_labels(distances, indices)
        
        # stopping condition
        # if np.array_equal(labels, prev_labels):
        #     break
        print(indices_results)
        print(indices_results.count(indices))

        if indices_results.count(indices) > 2:
            break
        
        # calculate new centroids
        for cluster_indx in range(len(indices)):
            # members = X[labels == indices[cluster_indx]]
            members = [ i  for i, x in enumerate(labels) if x == indices[cluster_indx]]
            indices[cluster_indx] = new_centroid(X, members, indices)
            #centroids[cluster_indx,:] = np.mean(members,axis=0)
        indices_results.append(indices)
        # keep the labels for next round's usage
        # prev_labels = np.argmin(distances,axis=1)
        #prev_labels = labels
        indices_results.append(indices)
    
    return labels,indices

res = kmeans(matrix_distance, 4)
print(res)
np.savetxt("k4.csv", res[0], delimiter=",")