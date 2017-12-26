from textblob import TextBlob as tb #text Bynary Large Object
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

n = 2
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
    node_position = current_node[1] # get the position of the element in the 
    for node in matrix:
        distance = node[0][0][node_position]
        if (1-distance) < epsilon: # inverse to obtain the right distance!
            neighbourPts.append(node[1])
    print(neighbourPts)
    return neighbourPts

def expandCluster(node, neighbour_nodes, clusters, c_n,eps, MinPts, matris, visited):
    clusters[c_n].append(node)
    for n_node in neighbour_nodes:
        if n_node[1] not in visited:
            neighbour_node_2 = regionScan(n_node, epsilon, matrix)
            if len(neighbour_node_2) >= MinPts:
                neighbour_nodes += neighbour_node_2
        if n_node[1] not in (i for i in clusters):
            clusters[c_n].append(n_node[1])


def DBSCAN(matrix, epsilon, min_nodes):
    noise = []
    visited = []
    clusters = []
    c_n = -1 #cluster number or position
    for node in matrix:
        visited.append(node[1])
        neighbour_nodes = regionScan(node, epsilon, matrix)
        if len(neighbour_nodes) < min_nodes:
            noise.append(node[1])
        else:
            clusters.append([])
            c_n += 1
    print("no. of clusters: " , len(clusters))
    print("length of noise:", len(noise))
            

DBSCAN(matrix, 0.5, 4)

