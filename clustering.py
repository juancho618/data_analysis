from textblob import TextBlob as tb #text Bynary Large Object
from functools import reduce
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from csv_helper import CSVHelper
import numpy as np
import random

def createMatrix():
    tweets = CSVHelper.load_csv("clean_tweets.csv")
    tweetOrdered = list(map(lambda x: x.split(','), tweets))
    documents = list(map(lambda x: x[1].strip(), tweetOrdered)) #getting just the tweet
    matrix = []

    # TF_IDF Matrix creation
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
    for i, document in  enumerate(documents):
        similarity = cosine_similarity(tfidf_matrix[i:i+1], tfidf_matrix)
        matrix.append((similarity.tolist(), i))
    return(matrix)


def regionScan(current_node, epsilon, matrix):
    neighbourPts = []
    node_position = current_node # get the position of the element in the 
    for node in matrix:
        distance = node[0][0][node_position]
        if (1-distance) < epsilon: # inverse to obtain the right distance!
            neighbourPts.append(node[1])
    return neighbourPts

def expandCluster(node, neighbour_nodes, clusters, c_n, epsilon, MinPts, matrix, visited):
    clusters[c_n].append(node[1])
    for n_node in neighbour_nodes:
        if n_node not in visited:
            visited.append(n_node)
            neighbour_node_2 = regionScan(n_node, epsilon, matrix)
            if len(neighbour_node_2) >= MinPts:
                for node_2 in neighbour_node_2:
                    if node_2 not in neighbour_nodes:
                        neighbour_nodes.append(node_2) 
        if n_node not in (reduce(lambda x,y: x+y,clusters)):
            clusters[c_n].append(n_node)


def DBSCAN(matrix, epsilon, min_nodes):
    noise = []
    visited = []
    clusters = []
    c_n = -1 #cluster number or position
    for node in matrix:
        if node[1] not in visited:
            visited.append(node[1])
            neighbour_nodes = regionScan(node[1], epsilon, matrix)
            if len(neighbour_nodes) < min_nodes:
                noise.append(node[1])
            else:
                clusters.append([])
                c_n += 1
                expandCluster(node, neighbour_nodes, clusters, c_n,epsilon, min_nodes, matrix, visited)
    print("no. of clusters: " , len(clusters))
    print("length of noise:", len(noise))
    #print("clusters " , clusters)
    # print("noise " , noise)
    #return({'clusters': len(clusters), 'noise': len(noise)})
    return(clusters)    

# matrix = createMatrix()
# res = DBSCAN(matrix, 0.6, 10)

#np.savetxt("clust-e6-n10.csv", res, delimiter=",")


