# This is solution to collections_counter problem
# https://www.hackerrank.com/challenges/decorators-2-name-directory
# Useful reference: http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
from operator import itemgetter

#Variation One
def sort_by_age(func):
    def formatter(data):
    	data.sort(key=itemgetter(1))
    	return func(data)
    return formatter
    
    
@sort_by_age
def format_name(data):
	print( '\n'.join( ['Mr. ' + name if gender == 'M' else 'Ms. ' + name for name, _ , gender in data] ) )


#Variation Two
def format_greeting(func):
	def formatter(data):
		data = [['Mr. ' + name if gender == 'M' else 'Ms. ' + name, age] for name, age , gender in data]
		return func(data)
	return formatter
  
  
@format_greeting
def sort_by_age(data):
	data.sort(key=itemgetter(1))
	for greeting, _ in data:
		print(greeting)
    
#Input
count = int(raw_input())
data = []
for _ in range(count):
    row = raw_input().split(' ')
    data.append( [ row[0] + ' ' + row[1], int(row[2]), row[3] ] )

format_name(data) # or sort_by_age(data)
    
