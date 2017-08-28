# Options to call method using kwargs
def multiply(num_one, num_two):
    return num_one * num_two

print(multiply(27, 2))
print(multiply(27, num_two=2))
print(multiply(num_one=27, num_two=2))
print(multiply(num_two=2, num_one=27))

#not allowed
#print(multiply(num_one=27, 2))
#print(multiply(2, num_one=27))


def multiply(**kwargs):
    if kwargs:
        result = 1
        for item in kwargs.keys():
            result *= int(kwargs[item])
        return result

print(multiply(num_one=2, num_two=3, num_three=4))
print(multiply())
