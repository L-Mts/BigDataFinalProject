#!/usr/bin/env python
# coding: utf-8

# In[18]:


import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "climate change min_faves:10 until:2022-01-01 since:2021-01-01 -filter:links -filter:replies"

limit = 100000
tweets = []
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.rawContent])

df = pd.DataFrame(tweets, columns=['Date', 'Tweet'])
    
df.to_csv('scraped-tweets.csv', index = False, encoding = 'utf-8')
    


# In[ ]:





# In[ ]:




