#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import numpy as np
import re

dfhh = pd.read_csv('Data_m_y_notclean2.csv')

dfhh


# In[36]:


from nltk.corpus import stopwords
df = pd.read_csv('Data_m_y_notclean2.csv')
def clean(x):
    x = x.lower()
    x = re.sub('(@[a-zA-Z0-9 _]+)|([^A-Za-z0-9 _])', '', x)
    stop = stopwords.words('english')
    x = [word for word in x.split() if x not in stop]
    return " ".join(x)


df['new_text'] = df.apply(lambda x: clean(x.Tweet), axis=1)


# In[37]:


df


# In[38]:


df_new=df.drop(['Tweet'], axis=1)


# In[39]:


df_new


# In[40]:


df_new.to_csv('all_df_mth.csv')


# In[41]:


from datetime import timedelta as dt

df_jan2 = df_new.loc[(df_new['Month'] == 'Jan')]
df_feb2 = df_new.loc[(df_new['Month'] =='Feb' )]
df_mar2 = df_new.loc[(df_new['Month'] == 'Mar')]
df_apr2 = df_new.loc[(df_new['Month'] == 'Apr')]
df_may2 = df_new.loc[(df_new['Month'] == 'May')]
df_jun2 = df_new.loc[(df_new['Month'] == 'Jun')]
df_jul2 = df_new.loc[(df_new['Month'] == 'Jul')]
df_aug2 = df_new.loc[(df_new['Month'] == 'Aug')]
df_sep2 = df_new.loc[(df_new['Month'] == 'Sep')]
df_oct2 = df_new.loc[(df_new['Month'] == 'Oct')]
df_nov2 = df_new.loc[(df_new['Month'] == 'Nov')]
df_dec2 = df_new.loc[(df_new['Month'] == 'Dec')]


# In[42]:


df_jan2.to_csv('df_jan2.csv')
df_feb2.to_csv('df_feb2.csv')
df_mar2.to_csv('df_mar2.csv')
df_apr2.to_csv('df_apr2.csv')
df_may2.to_csv('df_may2.csv')
df_jun2.to_csv('df_jun2.csv')
df_jul2.to_csv('df_jul2.csv')
df_aug2.to_csv('df_aug2.csv')
df_sep2.to_csv('df_sep2.csv')
df_oct2.to_csv('df_oct2.csv')
df_nov2.to_csv('df_nov2.csv')
df_dec2.to_csv('df_dec2.csv')


# In[ ]:




