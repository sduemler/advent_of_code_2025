from math import sqrt

input = open("day8/input.txt", "r")
lines = input.readlines()
junctions = []
completeJunctions = []
distances = {}

for line in lines:
    line = list(map(int,line.rstrip().split(',')))
    junctions.append(line)

# calculate all the distances between each of the junctions
# make a map of the distances, with the distance as the key and the two points as the value
# sort the keys, then go through the dict, adding each to the junction 

for j in junctions:
    for k in junctions:
        if j != k:
            distance = sqrt((j[0]-k[0]) ** 2 + (j[1]-k[1]) ** 2 + (j[2]-k[2]) ** 2)
            distances[distance] = [j, k]

closest = sorted(list(distances.keys()))

for x in range(10):
    print(distances[closest[x]])
    if len(completeJunctions) == 0:
        completeJunctions.append(distances[closest[x]])
    for y in range(len(completeJunctions)):
        # if they are both in the same junction do nothing
        # if they are in different junctions, combine the two
        # if only one is in a junctions, add the other to it
        # if neither are in it then add them as a new junction

            