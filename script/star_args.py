# *args materialise the list/tuple of the generator
def print_numbers(stmt, *values):
    if not values:
        print(stmt)
    else:
        print('{:s}: {:s}'.format(stmt, ', '.join(str(x) for x in values)))


def generate_number():
    for item in range(1, 10):
        yield item

print_numbers('This are my numbers', 1,2, 3)
print_numbers('This are my numbers', *[1,2, 3])
print_numbers('This are my numbers', *generate_number())
