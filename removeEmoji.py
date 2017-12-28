import re
import csv
text = u'This dog \U0001f602 🍡🍡🙇💮'
print(text) # with emoji

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF" 
        u"\U00002600-\U000027BF"
        u"\U0001f300-\U0001f64F"
        u"\U0001f680-\U0001f6FF"
        u"\u2600-\u27BF"
                            "]+", flags=re.UNICODE)
print(emoji_pattern.sub(r'', text)) # no emoji


#b=read.csv("example.csv"), row.names = FALSE)