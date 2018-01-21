from csv_helper import CSVHelper
import re
import nltk
import numpy
#nltk.download()
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
tknz = TweetTokenizer()  #Tokenization
tweets = CSVHelper.load_csv("Tweets_2016London.csv") #Load the provided CSV file
clean_tweets = []
#specify the format of the URL so we can remove it later
url_expression = 'http[s]?[:]?//(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
#remove emojis
emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF" 
        u"\U00002600-\U000027BF"
        u"\U0001f300-\U0001f64F"
        u"\U0001f680-\U0001f6FF"
        u"\u2600-\u27BF""]+", flags=re.UNICODE)
wordnet_lemmatizer = WordNetLemmatizer()
for t in tweets:
    stop = set(stopwords.words('english')) #stop words!
    framents = tknz.tokenize(t)
    clean_fragments = []
    for f in framents:
        if f not in stop: # not included in the stop words
            f = emoji_pattern.sub(r'', f)
            f = f.lower() #lowercase fragment
            f = re.sub(r'[.,"!~_:|?\']+', '', f,flags=re.MULTILINE) # Special characters
            f =  re.sub(r'\.\.\.', '', f,flags=re.MULTILINE) # 3 dots
            f = re.sub(url_expression, '', f,flags=re.MULTILINE) # links
            f = re.sub(r'@[a-z,A-Z,0-9 ]*', '', f, flags=re.MULTILINE) #clean at person references
            f = re.sub(r'RT @[a-z,A-Z]*: ', '', f, flags=re.MULTILINE) #Remove retweets
            f = wordnet_lemmatizer.lemmatize(f)
            if f:
                clean_fragments.append(f) #we append the cleaned tweet to clean_fragment vector
    clean_tweets.append(" ".join(clean_fragments)) #append the result to clean_tweets

num = 326
tweet = tweets[num]
c_tweet =  clean_tweets[num]
clean_array =  numpy.asarray(clean_tweets)

# Export the cleaned tweets to a new csv file.Pandas Library is used
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