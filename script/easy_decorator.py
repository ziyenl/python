def decorator_func(func):
    def helper(data):
        data = data + ' b. come before print_data '
        return func(data)
    return helper


@decorator_func
def print_data(data):
    data = data + ' c. come after decorator_func'
    return data

print(print_data('a. I am data '))
