from textblob import TextBlob as tb #text Bynary Large Object
import math

#ref link: https://lizrush.gitbooks.io/algorithms-for-webdevs-ebook/content/chapters/tf-idf.html
# http://blog.christianperone.com/2013/09/machine-learning-cosine-similarity-for-vector-space-models-part-iii/   cosine distances
# http://www.jonathanzong.com/blog/2013/02/02/k-means-clustering-with-tfidf-
# distance dbscan: https://github.com/chiragnagpal/simple-DBScan/blob/master/dbscan.py

def tf(word, blob): # fuction to count te term frecuency.
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist): # count the word ocurance in the document list.
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist): #inverse document fequency.
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)


document1 = tb("""RT @brides: These are 5 hidden jobs no one one tells about one maids-of-honor one about. You're welcome: jobs http://t.co/qybBewFDre
This brides week on brides twitter: One new brides follower via http://t.co/0NP5Wz70Op""")

document2 = tb("""Python, from the Greek word (Ï€ÏÎ¸Ï‰Î½/Ï€ÏÎ¸Ï‰Î½Î±Ï‚), is a genus of
nonvenomous pythons[2] found in Africa and Asia. Currently, 7 species are
recognised.[2] A member of this genus, P. reticulatus, is among the longest
snakes known.""")

document3 = tb("""The Colt Python is a .357 Magnum caliber revolver formerly
manufactured by Colt's Manufacturing Company of Hartford, Connecticut.
It is sometimes referred to as a "Combat Magnum".[1] It was first introduced
in 1955, the same year as Smith & Wesson's M29 .44 Magnum. The now   discontinued
Colt Python targeted the premium revolver market segment. Some firearm
collectors and writers such as Jeff Cooper, Ian V. Hogg, Chuck Hawks, Leroy
Thompson, Renee Smeets and Martin Dougherty have described the Python as the
finest production revolver ever made.""")

bloblist = [document1, document2, document3,] # document list


for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words} #creates a dictionary with all the words!
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True) #score items create tupples and sort by tfidf, DESC
    for word, score in sorted_words[:3]: # Select top 3 words
        print("Word: {}, TF-IDF: {}".format(word, round(score, 5))) #print the rounded number with 5 decimals.
