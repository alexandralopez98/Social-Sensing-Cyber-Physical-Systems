import tweepy
import time
import twitter_credentials as TC

auth = tweepy.OAuthHandler(TC.CONSUMER_KEY, TC.CONSUMER_SECRET)
auth.set_access_token(TC.ACCESS_TOKEN, TC.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

USER_IDS = [34373370, 26257166, 12579252]


# Try to get 20 followers of each user if rate limit error then we wait 15 mins
i = 0
while(i<3):
    count = 0 
    print("20 Followers of " + str(api.get_user(USER_IDS[i]).screen_name) + ":") 
    try:
        # Get 20 followers
        for follower in api.followers(USER_IDS[i]):
            if count<20:
                print(follower.screen_name)
            else:
                break
        i = i + 1
    except tweepy.error.RateLimitError:
        # Wait 15 mins 
        time.sleep(60*15) 
    print(" ")


i = 0
while(i<3): 
    count = 0 
    print("20 Friends of " + str(api.get_user(USER_IDS[i]).screen_name) + ":")
    try:
        for friend in api.friends(USER_IDS[i]):
            if count<20:
                print(friend.screen_name)
            else:
                break
        i = i + 1
    except tweepy.error.RateLimitError:
        time.sleep(60*15)
    print(" ")





