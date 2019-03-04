import numpy as np
import random
import operator
import json


''' HELPER FUNCTIONS TO FACILITATE CALCULATIONS'''
def calcS(i):
	return(sum(sensingMat[i])/2000)

def calcZ(j):
	Z = (calcA(j)*d)/float((calcA(j)*d)+(calcB(j)*(1-d)))
	return(Z)
	
def calcA(j):
	i = 0
	Atj = 1
	while i < 20:
		Atj *= pow(A[i], sensingMat[i][j]) * pow((1-A[i]), (1-sensingMat[i][j]))
		i += 1
	return Atj

def calcB(j):
	i = 0
	Btj = 1
	while i < 20:
		Btj *= pow(B[i], sensingMat[i][j]) * pow((1-B[i]), (1-sensingMat[i][j]))
		i += 1
	return Btj

'''_______________________________________________________________________________'''


sources = set()
with open("Tweets.txt") as json_file:
    for line in json_file:
        tweet = json.loads(line)
        sources.add(tweet['id'])


numSources = len(sources)
numVars = 25				# Manualy counted

# Create sensing mat
sensingMat = np.zeros((numSources,numVars))

i = 0
# Populate the Sensing Matrix
for id in sources:
	# For every source see what claim it points to.
	#print("Mapping ID: "+ str(id) + " to index "+ str(i))
	data = open("Cluster_Result_Tweetsid.txt")
	for line in data:
		line = line.split(":")
		var = int(line[0])-1	# Get cluster (source) ID
		for num in line[1].rstrip().split(","):
			if(id==int(num)):
				sensingMat[i][var] = 1	
	i += 1


#print(sensingMat)



# Initialize theta
A = list(range(numSources)) 
B = list(range(numSources))
Z = list(range(numVars))
d = 0.5
for i in range(numSources):
	A[i] = calcS(i)
	B[i] = A[i]*0.5


counter = 0
while counter < 20:

	counter += 1
	j = 0
	# Compute Z
	while j < numVars:
		Z[j] = calcZ(j) 
		j+=1

	i = 0
	# Update a,b, and d
	while i  < numSources:
		obsZ = 0
		totalZ = sum(Z)
		for j in range(numVars):
			if(sensingMat[i][j]==1):
				obsZ += Z[j]
		# Calculate new A
		try:
			A[i] = obsZ/float(totalZ)
		except ZeroDivisionError:
			A[i]=0
		# Calculate new B
		try:
			B[i] = (sum(sensingMat[i])-obsZ)/float(numVars - totalZ)
		except ZeroDivisionError:
			B[i]=0
		# Calculate new D
		d = totalZ/ float(numVars)
		i += 1


scoreDict = dict()
# Report on true or false for each source
for j in range(numVars):
	scoreDict[j+1] = Z[j]



sorted_by_value = sorted(scoreDict.items(), key=operator.itemgetter(1), reverse=True)
for cluster in sorted_by_value:
	print(str(cluster[0])+": "+ str(cluster[1]))
