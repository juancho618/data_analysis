from csv_helper import CSVHelper
from functools import reduce
from textblob import TextBlob as tb #text Bynary Large Object


def tf(word, blob): # fuction to count te term frecuency.
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist): # count the word ocurance in the document list.
    return sum(1 for blob in bloblist if word in blob)

data = CSVHelper.load_csv("dbscan_results.csv")

tweets = CSVHelper.load_csv("clean_tweets.csv")
tweetOrdered = list(map(lambda x: x.split(','), tweets))

#Get real clean tweets
listDoc = []
for cluster in data:
    sub =[]
    cluster = [int(item) for item in cluster if (item != ',' and item != ' ')]
    for t in cluster:
        sub.append(tb(tweetOrdered[int(t)][1].strip()))
    listDoc.append(sub)



resultWords = []
for x,cluster in enumerate(listDoc):
    scores = {}
    blobList = reduce(lambda x,y: x+y,cluster)
    print(len(cluster))
    for i, blob in enumerate(cluster):
        print(i)
        scores = {word: tf(word, blobList) for word in blob.words}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    resultWords.append({'cluster'+str(x): sorted_words[0][0]})
    print(sorted_words)

print(resultWords)


        
