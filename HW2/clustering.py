import json
import math

def jaccard_similarity(x,y):
 
    intersection = len(set.intersection(*[set(x), set(y)]))
    union = len(set.union(*[set(x), set(y)]))
    return intersection/float(union)




tweets = {}
newCentroids = []
oldCentroids = []
centroidFile = open("InitialSeeds.txt")
clusters = {}
# Get initial centroid IDs
for line in centroidFile:
    oldCentroids.append(int(line.rstrip().rstrip(',')))


newCentroids = oldCentroids


# Get all tweets
with open("Tweets.json") as json_file:
    for line in json_file:
        tweet = json.loads(line)
        tweets[tweet['id']]= tweet['text']


while(1):
    clusters = {}
    # Create empty cluster dict
    for cent in oldCentroids:
        clusters[cent]= []

    # For each tweet cluster, label it by calculating distance to nearest centroid
    for ID in tweets:
        minDist = 1000 # arbitrary big num
        count = 0
        # For each centroid calculate jaccard distance with tweet
        for cent in oldCentroids:
            newDist = 1-jaccard_similarity(tweets[ID].split(" "), tweets[cent].split(" "))
            # If closer to new centroid then update best cluster
            if(newDist <= minDist):
                minDist = newDist
                clusterPrediction = count
            count+=1
    
        # Place in the optimal cluster after comparing to all centroids
        clusters[oldCentroids[clusterPrediction]].append(ID)



    newCentroids = []

    # Calculate new centroid for each cluster by getting sum of distance to every other tweet in that cluster
    for i in range(25):
        tweetIndex = 0
        minSumDist = 1000  # Arbitrary big num
        newCentroidIndex = -1
        # For tweet in current cluster
        for ID1 in clusters[oldCentroids[i]]:
            sumDist = 0
            # Calculate sum of dist to every other tweet in same cluster
            for ID2 in clusters[oldCentroids[i]]:
                newDist = 1-jaccard_similarity(tweets[ID1].split(" "), tweets[ID2].split(" "))
                sumDist+=newDist
            # If the calculated sum is less than any sum seen before
            if sumDist <= minSumDist:
                # Update the minimum sum
                minSumDist = sumDist
                newCentroidIndex = tweetIndex    
            tweetIndex+=1

        # Assign new centroid
        newCentroids.append(clusters[oldCentroids[i]][newCentroidIndex])

    # If new and current old centroids are the same we are done
    if(newCentroids == oldCentroids):
        break
    else:
       oldCentroids = newCentroids
       newCentroids = []


# When centroids have not changed anymore then we say clustering is done
clusterID = 0
for centroid in newCentroids:
    print(str(clusterID) + ": " +str(clusters[centroid]))
    clusterID+=1



