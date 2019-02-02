import tweepy

import twitter_credentials as TC

auth = tweepy.OAuthHandler(TC.CONSUMER_KEY, TC.CONSUMER_SECRET)
auth.set_access_token(TC.ACCESS_TOKEN, TC.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

USER_IDS = [34373370, 26257166, 12579252]

for ID in USER_IDS:
    print(api.get_user(ID))


