# new approach of string formatting in python 3.6 and above
# it allows interjection of variables from local environment

animal = "cats"
measurement = "weight"
quantity = 65.423

print( f"{animal}\'s average {measurement} is {quantity:.2f} kg")

