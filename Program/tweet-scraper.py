import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "web scraping"  
for tweet in sntwitter.TwitterSearchScraper(query).get_items():   print(vars(tweet))   break 

limit = 1000
tweets = []

for tweet in sntwitter.TwitterSearchScraper(query).get_items():   if len(tweets) == limit:       break   else:       tweets.append([tweet.date, tweet.user.username, tweet.content])

df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])#print(df)

df.to_csv('scraped-tweets.csv', index=False, encoding='utf-8')

df.to_json('scraped-tweets.json', orient='records', lines=True)