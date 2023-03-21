#!/usr/bin/env python
# coding: utf-8

# In[45]:


#!pip install wordcloud


# In[72]:


import pandas as pd
import bs4
import re
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud  
data = pd.read_csv("Allmergedcsv2.csv")


# In[73]:


data


# In[74]:


def rem_hashtags(text):
    processed_text = re.sub(r" #natural disater,#natural disaster, #climate change", "", text)
    processed_text = " ".join(processed_text.split())
    return processed_text
data['Tweet'] = data['Tweet'].apply(lambda x:rem_hashtags(x))
#removing tagged users from the tweets
def remove_users(text):
    processed_text = re.sub(r'@\w+ ?',"",text)
    processed_text = " ".join(processed_text.split())
    return processed_text
data['Tweet'] = data['Tweet'].apply(lambda x:remove_users(x))
#removing hyperlinks mentioned in the tweets
def remove_links(text):
    processed_text = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", text)
    processed_text = " ".join(processed_text.split())
    return processed_text
data['Tweet'] = data['Tweet'].apply(lambda x:remove_links(x))
#removing punctuations in the tweets
def remove_punct(text):
    punctuations = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    text  = "".join([char for char in text if char not in punctuations])
    text = re.sub('[0-9]+', '', text)
    return text
data['Tweet'] = data['Tweet'].apply(lambda x: remove_punct(x))
#making all tweets lowercase
def lowercase_word(text):
    text  = "".join([char.lower() for char in text])
    return text
data['Tweet'] = data['Tweet'].apply(lambda x: lowercase_word(x))


# In[75]:


tweet_All = " ".join(tweet for tweet in data['Tweet'])
fig, ax = plt.subplots(1, 1, figsize  = (30,30))
# Create and generate a word cloud image:
wordcloud_ALL = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(tweet_All)
# Display the generated image:
ax.imshow(wordcloud_ALL, interpolation='bilinear')
ax.axis('off')


# In[77]:


from textblob import TextBlob
#from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
def get_tweet_sentiment(data): 
    if data > 0: 
        return 'positive'
    elif data == 0: 
        return 'neutral'
    else: 
        return 'negative'
tweets = [TextBlob(tweet) for tweet in data['Tweet']]
data['polarity'] = [b.sentiment.polarity for b in tweets]
data['subjectivity'] = [b.sentiment.subjectivity for b in tweets]
data['sentiment'] = data['polarity'].apply(get_tweet_sentiment)
data['sentiment'].value_counts()


# In[54]:


#!pip install textblob 


# In[ ]:




