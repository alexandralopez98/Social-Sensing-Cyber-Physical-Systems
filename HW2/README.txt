I used python 3 to run my programs
Both can be run with no input necessary.

Task 1:	Run python ./clustering.py to run it
	Uses the centroids given to us as the initial centroids.
	If different list is wanted then it has to be changed in the code.
	

Task 2:
	I created a program called initialize.py that implements K-Means++ centroid initilization.
	Main idea is that it picks a random centroid at first and then picks a point that is furthest
	from the existing centroids as a new centroid and repeats until we have 25 centroids. 

	This program outputs a list of 25 tweet IDs which will act as the centroids.
	This list can then be used in my first program as the centroids list. (This is how the second output file was generated)

	Run python ./initialize.py to run it



