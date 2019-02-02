import tweepy
import time
import twitter_credentials as TC

auth = tweepy.OAuthHandler(TC.CONSUMER_KEY, TC.CONSUMER_SECRET)
auth.set_access_token(TC.ACCESS_TOKEN, TC.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
count = 1

# Query to get 50 tweets with either Indiana or Weather in them
for tweet in tweepy.Cursor(api.search, q = "Indiana OR Weather").items(50):
    print(str(count) +". "+ tweet.text)
    count+=1
