import numpy as np
import random


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

numSources = 30
numVars = 2000

data = open("SCMatrix_Submit")
sensingMat = np.zeros((numSources,numVars))

# Populate the Sensing Matrix
for line in data:
	line = line.rstrip().split(",")
	sensingMat[int(line[0])-1][int(line[1])-1] = 1	


# Initialize theta
A = range(numSources) 
B = range(numSources)
Z = range(numVars)
d = random.uniform(0,1)
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


# Report on true or false for each source
for j in range(numVars):
	if Z[j] >= 0.5:
		print(str(j+1) +", 1")
	else:
		print(str(j+1) +", 0")