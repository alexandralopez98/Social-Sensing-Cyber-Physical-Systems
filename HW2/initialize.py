# Manuel Marroquin
# 2/17/19
# Implementation of K++ centroid initialization from scratch for Boston Bombing tweet clustering

import json
import math
import random

def jaccard_similarity(x,y):
    intersection = len(set.intersection(*[set(x), set(y)]))
    union = len(set.union(*[set(x), set(y)]))
    return intersection/float(union)




tweets = {}
centroids = []

# Get all tweets
with open("Tweets.json") as json_file:
    for line in json_file:
        tweet = json.loads(line)
        tweets[tweet['id']]= tweet['text']



# Pick a random initial centroid
centroids.append(random.choice(list(tweets.keys())))

while(1):
    centMaxDist = -1

    # For each tweet
    for tweetID in tweets:
        centMinDist = 100

        centIndex = 0
        closestCentIndex = -1

        # Find the centroid it is closest to
        for centID in centroids:
            centDist = 1-jaccard_similarity(tweets[centID],tweets[tweetID])
            # If we find a centroid thats closer than those seen before, remember it
            if centDist < centMinDist and centID != tweetID:
                centMinDist = centDist
                closestCentIndex = centIndex
            centIndex+=1



        # Check if this tweet is the furthest from its respective centroid than those we have seen

        furthestCentDist = 1-jaccard_similarity(tweets[centroids[closestCentIndex]],tweets[tweetID])
        # If it is then we mark it as a potential new centroid
        if(furthestCentDist >= centMaxDist and tweetID not in centroids):

            centMaxDist = furthestCentDist
            furthestTweetID = tweetID

    centroids.append(furthestTweetID)
    # End after 25 centroids
    if(len(centroids) == 25):
        break
    
for ID in centroids:
    print(str(ID) +",")
