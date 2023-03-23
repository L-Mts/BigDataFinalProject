#!/usr/bin/env python
# coding: utf-8

# In[57]:


import pandas as pd

#data = pd.read_csv("scraped-tweets-apr2.csv")
#data = pd.read_csv("scraped-tweets-aug2.csv")
#data = pd.read_csv("scraped-tweets-dec2.csv")
#data = pd.read_csv("scraped-tweets-feb2.csv")
#data = pd.read_csv("scraped-tweets-jan2.csv")
#data = pd.read_csv("scraped-tweets-jul2.csv")
#data = pd.read_csv("scraped-tweets-jun2.csv")
#data = pd.read_csv("scraped-tweets-mai2.csv")
#data = pd.read_csv("scraped-tweets-mar2.csv")
#data = pd.read_csv("scraped-tweets-oct2.csv")
#data = pd.read_csv("scraped-tweets-sep2.csv")
data = pd.read_csv("scraped-tweets-nov2.csv")


#data = pd.read_csv("Allmergedcsv2.csv")
tweets = data["Tweet"]


# In[58]:


def lowercase_word(text):
    text  = "".join([char.lower() for char in text])
    return text
data['Tweet'] = data['Tweet'].apply(lambda x: lowercase_word(x))


# In[59]:


def count_exact_words(df, column_name, word):
    data["Tweet"] = data["Tweet"] + '.'
    return word, df['Tweet'].str.count(r'({word})'.format(word=word)).sum()

print(count_exact_words(data, 'Tweet', 'globalwarming'))
print(count_exact_words(data, 'Tweet', 'global warming'))
print(count_exact_words(data, 'Tweet', 'climatechange')) 

print(count_exact_words(data, 'Tweet', 'climate change')) 
print(count_exact_words(data, 'Tweet', 'natural disaster')) 
print(count_exact_words(data, 'Tweet', 'naturaldisaster')) 


# In[ ]:




