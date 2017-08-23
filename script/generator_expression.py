# Favor usage of generator expression for large comprehensions
# open a file and write a range of random number a len words and get the length of the lines
import random
with(open("temp.txt",'r+'))as f:
    for i in range(0,5):
        f.write('a' * random.randint(0,100) + '\n')

gen_list = (x for x in open("temp.txt").readlines())
print(len(next(gen_list)))


# get the square root of the length len
square_list = ((len(x), len(x)**0.5) for x in gen_list)
print(next(square_list))
print(next(square_list))
print(next(square_list))
print(next(square_list))
