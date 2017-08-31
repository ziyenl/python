#!/bin/python3
# https://www.hackerrank.com/contests/101hack51/challenges/charging-the-batteries/problem
# Algorithm
# 1. Start from 0,0 and find distance of each point in reference to 0,0 to simulate walking around in the continuous connected line
# 2. Sort the coordinate
# 3. To cover for distance between the last coordinate with first coordinate, we need to add "artificial distances" to reflect 
# equal distance between points as the original set of distance
# 4. Get distance between the differing points e.g. point 1 and point 3 and get the shortest distance of them.

import sys

if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    coordinates = []
    for a0 in range(m):
        x, y = input().strip().split(' ')
        x, y = [int(x), int(y)]
        if x == 0:
            coordinates.append(y)
        elif y == n:
            coordinates.append(n + x)
        elif x == n:
            coordinates.append(2 * n + (n-y))
        elif y == 0:
            coordinates.append(3 * n + (n-x))
    # allow traversal of another round to check the distance between nodes
    coordinates.sort()
    coordinates = coordinates + [c + (4 * n) for c in coordinates]
    current_best = sys.maxsize
    for idx in range(len(coordinates)-k+1):
        diff = coordinates[idx+k-1] - coordinates[idx]
        if diff < current_best:
            current_best = diff
    print(current_best)
            
        
        
        
