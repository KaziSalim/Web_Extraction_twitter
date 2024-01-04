# pip install tweepy

# Twitter Extraction
import pandas as pd
import tweepy
from tweepy import OAuthHandler
 

consumer_key = "DQn3P0CW9rzIh8P3wg1d8gt4v"
consumer_secret = "6St9b0YT3B0S7LMkcTRRItjYJTbmF2UNK76aspfcn6dm1z601U"
access_token = "1742516067527012352-Gx0GJETdlwa2ivUq2sy5vZEUjEwjwV"
access_token_secret = "igz6anhAIbpGf18VBXhB8tsMOcMuqREL7qQu9vaxj2EpL"

# Calling API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)# Application programmer interface


# Provide the keyword related to which you want to pull the data e.g. "Python".
keyword = "ICC Cricket World Cup"

# Fetching tweets
tweets_keyword = api.search_tweets(keyword, count = 100, lang = 'en',
                            exclude = 'retweets', tweet_mode = 'extended') #Changed
 
for item in tweets_keyword:
    print(item)
    
tweets_for_csv = [tweet.full_text for tweet in tweets_keyword] 


# 200 tweets to be extracted 
tweets_user = api.user_timeline(screen_name = "ShashiTharoor", count = 200)


for item in tweets_user:
    print(item)
# Create array of tweet information: username, tweet id, date/time, text 
tweets_for_csv1 = [tweet.text for tweet in tweets_user] 

# Saving the tweets onto a CSV file
# convert 'tweets' list to pandas DataFrame
tweets_df = pd.DataFrame(tweets_for_csv1, columns = ['Value'])

tweets_df.to_csv('tweets.csv')

import os
os.getcwd()
