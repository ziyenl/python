def memoize(func):
    ''' memoize fibonacci functions '''
    storage = {}
    def helper(n):
        if n not in storage.keys():
            storage[n] = func(n)
        return storage[n]
    return helper

def fibonacci(n):
    ''' recursive fibonacci calculation '''
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
n = int(raw_input())
fibonacci = memoize(fibonacci)
print(fibonacci(n))


