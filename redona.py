from nltk.tokenize import TweetTokenizer, sent_tokenize
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


'''tknzr = TweetTokenizer()
s0 = "This is a cooool #dummysmiley: :-) :-P <3 and some arrows < > -> <--"
print(tknzr.tokenize(s0))'''

text ="this’s a sent tokenize test. this is sent two. is this sent three? sent 4 is cool! Now it’s your turn."

#sent_tokenize knows what punctuation and characters mark the end of a sentence and the beginning of a new sentence.
sent_tokenize_list = sent_tokenize(text)
print(sent_tokenize_list)


print(word_tokenize("Hello World."))

#JJ: adjective or numeral, ordinal,IN: preposition or conjunction, subordinating,NNP: noun, proper, singular
#POS=part-of-speech tagging
print(nltk.pos_tag(text))

#lemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
b=wordnet_lemmatizer.lemmatize("dogs")
print(b)
print(wordnet_lemmatizer.lemmatize("churches"))
