#!/bin/python3
# Sort based on length followed by the number itself or it throws time out exception

import sys

n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
   unsorted_t = str(input().strip())
   unsorted.append(unsorted_t)
# your code goes here
sort_by_length_by_increment = lambda x : (len(x), x)
unsorted.sort(key=sort_by_length_by_increment)
for item in unsorted:
    print(item)

