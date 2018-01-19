from textblob import TextBlob as tb #text Bynary Large Object
from functools import reduce
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random


documents = (
"The sky is blue",
"The sun is bright",
"The sun in the sky is bright",
"We can see the shining sun, the bright sun"
)


tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
matrix = []

for i, document in  enumerate(documents):
    similarity = cosine_similarity(tfidf_matrix[i:i+1], tfidf_matrix)
    matrix.append((similarity.tolist(), i))
n = 1
epsilon = 0.5

#first part 
def selectRandom(k, list):
    random_select = []
    added = False
    for i in range(k):
        added = False
        while added == False:
            value = random.choice(list) 
            if value not in random_select:
                random_select.append(value)
                added = True
    return random_select

lista =  selectRandom(n, matrix) # select random m amount of elements.

def regionScan(current_node, epsilon, matrix):
    neighbourPts = []
    node_position = current_node # get the position of the element in the 
    for node in matrix:
        distance = node[0][0][node_position]
        if (1-distance) < epsilon: # inverse to obtain the right distance!
            print('adding node', node[1])
            neighbourPts.append(node[1])
    print(neighbourPts)
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
                print('adding noise')
                noise.append(node[1])
            else:
                clusters.append([])
                c_n += 1
                expandCluster(node, neighbour_nodes, clusters, c_n,epsilon, min_nodes, matrix, visited)
    print("no. of clusters: " , len(clusters))
    print("length of noise:", len(noise))
    print("clusters " , clusters)
    print("noise " , noise)
            

DBSCAN(matrix, 0.5, 2)
