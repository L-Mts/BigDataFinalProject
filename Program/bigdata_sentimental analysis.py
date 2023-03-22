#!/usr/bin/env python
# coding: utf-8

# In[45]:


#!pip install wordcloud


# In[220]:


import pandas as pd
import bs4
import re
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud  
data = pd.read_csv("Allmergedcsv2.csv")
#data = pd.read_csv("scraped-tweets-apr2.csv")
#data = pd.read_csv("scraped-tweets-aug2.csv")
#data = pd.read_csv("scraped-tweets-dec2.csv")
#data = pd.read_csv("scraped-tweets-feb2.csv")
#data = pd.read_csv("scraped-tweets-jan2.csv")
#data = pd.read_csv("scraped-tweets-jul2.csv")
#data = pd.read_csv("scraped-tweets-jun2.csv")
#data = pd.read_csv("scraped-tweets-mai2.csv")
#data = pd.read_csv("scraped-tweets-mar2.csv")
#ata = pd.read_csv("scraped-tweets-oct2.csv")
#data = pd.read_csv("scraped-tweets-sep2.csv")
#data = pd.read_csv("scraped-tweets-nov2.csv")


# In[221]:


data


# In[222]:


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


# In[223]:


data


# In[227]:


tweet_All = " ".join(tweet for tweet in data['Tweet'])
fig, ax = plt.subplots(1, 1, figsize  = (30,30))
# Create and generate a word cloud image:
wordcloud_ALL = WordCloud(max_font_size=50, max_words=70, background_color="white").generate(tweet_All)
# Display the generated image:
ax.imshow(wordcloud_ALL, interpolation='bilinear')
ax.axis('off')


# In[ ]:





# In[131]:


from textblob import TextBlob
#from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
def get_tweet_sentiment(data): 
    if data > 0: 
        return 'Pro'
    elif data == 0: 
        return 'Neutral'
    else :
        return 'Negative'
    
tweets = [TextBlob(tweet) for tweet in data['Tweet']]
data['polarity'] = [b.sentiment.polarity for b in tweets]
data['subjectivity'] = [b.sentiment.subjectivity for b in tweets]
data['sentiment'] = data['polarity'].apply(get_tweet_sentiment)
data['sentiment'].value_counts()


# In[58]:



len(data)


# In[59]:


#data['Tweet'] = data['Tweet'].str.lower()
#list_terms = data['Tweet'].unique()
#print(len(list_terms))
#list_terms


# In[60]:


#!pip install textblob 


# In[70]:


#import nltk

#import seaborn as sns
#import matplotlib.pyplot as plt 

# Style
#import matplotlib.style as style 
#sns.set(font_scale=1.5)
#style.use('seaborn-pastel')
#style.use('seaborn-poster')
#from PIL import Image
#style.use('seaborn-pastel')

#, axes = plt.subplots(ncols=2, 
                        # nrows=1, 
                        # figsize=(20, 10), 
                        # dpi=100)

#sns.countplot(data['sentiment'], ax=axes[0])

#=['Pro',  'Neutral', 'Negative'] 

#axes[1].pie(data['sentiment'].value_counts(),
           # labels=labels,
            #autopct='%1.0f%%',
           #shadow=True,
           # startangle=90,
           # explode = (0.1, 0.1, 0.1, 0.1))

#fig.suptitle('Tweet distribution', fontsize=20)
#plt.show()


# In[71]:


import pandas as pd
import bs4
import re
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud  
data_apr = pd.read_csv("scraped-tweets-apr2.csv")


# In[ ]:




