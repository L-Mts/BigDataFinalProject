import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(\"climat change\" OR \"natural disaster\" OR \"global warming\") lang:en until:2022-12-01 since:2022-11-01 -filter:links"
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    print(vars(tweet))
    break 

limit = 10000
tweets = []

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])#print(df)

df.to_csv('scraped-tweets-nov.csv', index=False, encoding='utf-8')

df.to_json('scraped-tweets-nov.json', orient='records', lines=True)