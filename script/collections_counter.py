# This is solution to collections_counter problem
# https://www.hackerrank.com/challenges/collections-counter
from collections import Counter

number_of_shoes = input()
available_shoe_sizes = input()
number_of_customers = input()

number_of_shoes = int(number_of_shoes)
available_shoe_sizes = available_shoe_sizes.split(' ')
available_shoe_sizes = [ int(item) for item in available_shoe_sizes ]
number_of_customers = int(number_of_customers)
counter = Counter(available_shoe_sizes)
total_earnings = 0

for item in range(number_of_customers):
    shoe_size_and_price = input()
    shoe_size_and_price = shoe_size_and_price.split(' ')
    shoe_size, price = [ int(item) for item in shoe_size_and_price ]
    if shoe_size in counter.keys() and counter[shoe_size] > 0:
        counter[shoe_size] -= 1
        total_earnings += price
     
print(total_earnings)
 
