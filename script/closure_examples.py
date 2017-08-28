def group_by_numbers(number):
    group = {4, 5, 6}
    if number in group:
        return (0, number)
    else:
        return (1, number)

list_numbers = [item for item in range(0,10)]

list_numbers.sort(key=group_by_numbers)

print(list_numbers)


def group_by_numbers_with_closure(number):
    group = {4, 5, 6}
    exist = False
    def helper(number):
        if number in group:
            nonlocal present
            exist = True
            return 0, number
        else:
            return 1, number
    number.sort(key=helper)
    return exist

sample_list = [1,2,3,4,5,6]
print(group_by_numbers(sample_list))
print(sample_list)

