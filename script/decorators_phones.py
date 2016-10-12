def format_phone_number(func):
    ''' Format phone number with a standardized prefix of +91 '''
	def formatter(numbers):
		formatted_numbers = []
		for number in numbers:
			if number.startswith('0'):
				number = number[1:]
			if len(number) >= 12:
				number = number[3:] if number.startswith('+') else number[2:]
			formatted_number = '+91 ' + number[:int(len(number)/2)] + ' ' + number[int(len(number)/2):]
			formatted_numbers.append(formatted_number)
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
  
