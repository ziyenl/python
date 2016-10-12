# This is solution to standardizing mobile number problem
# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators
def format_phone_number(func):
    ''' Format phone number with a standardized prefix of +91 '''
    def formatter(numbers):
        formatted_numbers = []
        for number in numbers:
        	formatted_numbers.append('+91 ' + number[-10:-5] + ' ' + number[-5:])
        return func(formatted_numbers)
    return formatter


@format_phone_number
def print_phone_number(phone_numbers):
	''' Print phone number in sorted order '''
	for number in sorted(phone_numbers):
		print( number )

count = int(raw_input())
phone_numbers = []
for number in range(count):
    phone_numbers.append(raw_input())
 
print_phone_number(phone_numbers)
