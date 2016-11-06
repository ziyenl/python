# This is solution for recursive fibonacci using memoize
# https://www.hackerrank.com/challenges/ctci-fibonacci-numbers
def memoize(func):
    storage = {}
    def helper(n):
        if n not in storage.keys():
            storage[n]=func(n)
        return storage[n]
    return helper

@memoize
def fibonacci(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
n = int(raw_input())
print(fibonacci(n))


