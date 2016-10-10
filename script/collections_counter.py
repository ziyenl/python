# This is solution to collections_counter problem
# https://www.hackerrank.com/challenges/collections-counter
from collections import Counter

def get_total_earnings(shoe_sizes, customers):
    '''Get total earnings'''
    total_earnings = 0
    counter = Counter(shoe_sizes)
    for item in range(customers):
        shoe_size, price = list( map(int, input().split(' ')) )
        if shoe_size in counter.keys() and counter[shoe_size] > 0:
            counter[shoe_size] -= 1
            total_earnings += price
    return total_earnings

number_of_shoes = int(input())
available_shoe_sizes = list( map(int, input().split(' ')) )
number_of_customers = int(input())
earnings = get_total_earnings(available_shoe_sizes, number_of_customers)
print(earnings)
