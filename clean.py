from csv_helper import CSVHelper
import re
from nltk.tokenize import TweetTokenizer
tknz = TweetTokenizer()
tweets = CSVHelper.load_csv("Tweets_2016London.csv")
clean_tweets = []
url_expression = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

for t in tweets:
    framents = tknz.tokenize(t)
    clean_fragments = []
    for f in framents:
        f = re.sub(r'[.,"!~]+', '', f,flags=re.MULTILINE) # Special characters
        f = re.sub(url_expression, '<link>', f,flags=re.MULTILINE) # Special characters
        clean_fragments.append(f)
    clean_tweets.append(" ".join(clean_fragments))

    # urls = re.findall(url_expression, t)
    # for u in urls:
    #     t = t.replace(u, '<link>')
    # clean_tweets.append(t)
        

num = 539
tweet = tweets[num]
c_tweet =  clean_tweets[num]


url = re.findall(url_expression, tweet)

print(tweet)
print(c_tweet)
print(url)
print(tknz.tokenize(tweet))


# links :
# https://stackoverflow.com/questions/26304191/get-the-document-name-in-scikit-learn-tf-idf-matrix
# https://www.youtube.com/watch?v=RPMYV-eb6lI