from csv_helper import CSVHelper
import re
import nltk
import numpy
nltk.download()
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
tknz = TweetTokenizer()
tweets = CSVHelper.load_csv("Tweets_2016London.csv")
clean_tweets = []
url_expression = 'http[s]?[:]?//(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

wordnet_lemmatizer = WordNetLemmatizer()
for t in tweets:
    stop = set(stopwords.words('english')) #stop words!
    framents = tknz.tokenize(t)
    clean_fragments = []
    for f in framents:
        if f not in stop: # not included in the stop words
            f = f.lower() #lowercase fragment
            f = re.sub(r'[.,"!~_:|?]+', '', f,flags=re.MULTILINE) # Special characters
            f = re.sub(url_expression, '', f,flags=re.MULTILINE) # links
            f = re.sub(r'@[a-z,A-Z,0-9 ]*', '', f, flags=re.MULTILINE) #clean at person references
            f = re.sub(r'RT @[a-z,A-Z]*: ', '', f, flags=re.MULTILINE) #Remove retweets
            f = wordnet_lemmatizer.lemmatize(f)
            if f:
                clean_fragments.append(f)
    clean_tweets.append(" ".join(clean_fragments))




num = 68
tweet = tweets[num]
c_tweet =  clean_tweets[num]
clean_array =  numpy.asarray(clean_tweets)

# Export to csv
import pandas as pd
df = pd.DataFrame(clean_array)
df.to_csv("file_path.csv")

url = re.findall(url_expression, tweet)

print(tweet)
print(c_tweet)
print(url)
print(tknz.tokenize(tweet))
print(tknz.tokenize(c_tweet))


# links :
# https://stackoverflow.com/questions/26304191/get-the-document-name-in-scikit-learn-tf-idf-matrix
# https://www.youtube.com/watch?v=RPMYV-eb6lI