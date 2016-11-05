# This is solution to collections_counter problem
# https://www.hackerrank.com/challenges/ctci-making-anagrams
from collections import Counter

def number_needed(a, b):
	''' number of characters needed to remove to produce anagrams '''
	common_total = 0
	counter_a = Counter(a)
	counter_b = Counter(b)
	for item in counter_b:
		if item in counter_a.iterkeys():
			common_total += min(counter_a[item], counter_b[item])
	differences = len(a) + len(b) - common_total * 2
	return differences

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
