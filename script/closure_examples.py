def group_by_numbers(number):
    group = {4, 5, 6}
    if number in group:
        return (0, number)
    else:
        return (1, number)

list_numbers = [item for item in range(0,10)]

list_numbers.sort(key=group_by_numbers)

print(list_numbers)

