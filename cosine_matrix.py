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

# print(matrix[1][0][0])
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
        if n_node not in visited:


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

            

regionScan(matrix[0], 0.5, matrix)

