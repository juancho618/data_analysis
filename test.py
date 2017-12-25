from textblob import TextBlob as tb #text Bynary Large Object
import math

#ref link: https://lizrush.gitbooks.io/algorithms-for-webdevs-ebook/content/chapters/tf-idf.html
# http://blog.christianperone.com/2013/09/machine-learning-cosine-similarity-for-vector-space-models-part-iii/   cosine distances

def tf(word, blob): # fuction to count te term frecuency.
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist): # count the word ocurance in the document list.
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist): #inverse document fequency.
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)


document1 = tb("""The sky is blue""")

document2 = tb("""The sun is bright""")

document3 = tb(""""The sun in the sky is bright""")

document4 = tb(""""We can see the shining sun, the bright sun""")

bloblist = [document1, document2, document3, document4] # document list

vector_words= []
for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words} #creates a dictionary with all the words!
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True) #score items create tupples and sort by tfidf, DESC
    # vector_words.append([lambda x: x[1], scores ])
    some = [item for x in scores]
    for word, score in sorted_words[:]: # Select top 3 words
        print("Word: {}, TF-IDF: {}".format(word, round(score, 5))) #print the rounded number with 5 decimals.

