# This is solution to the defaultdict problem
# https://www.hackerrank.com/challenges/defaultdict-tutorial
from collections import defaultdict


def print_result(dictionary, second_group ):
    ''' print result of groups to screen if they exist, else print -1 to screen '''
    for item in range( second_group ):
        s = input()
        if s in dictionary.keys():
            print( ' '.join( map(str, dictionary[s]) ) )
        else:
            print(-1)
    
    
def generate_defaultdict( first_group ):
    ''' generate default dict from first group '''
    dictionary = defaultdict(list)
    exist_c = False
    for item in range( first_group ):
        first = input()
        dictionary[first].append( item+1 )
    return dictionary
        
    
group_a, group_b = map( int, input().split(' ') )  
dictionary=generate_defaultdict( group_a )
print_result(dictionary, group_b)
    
        
        
    
    
    
