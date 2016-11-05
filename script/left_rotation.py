# This is solution to the left rotation in arrays
# https://www.hackerrank.com/challenges/ctci-array-left-rotation

def array_left_rotation(a, n, k):
    rotation = k % n
    return a[rotation:] + a[:rotation]

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
