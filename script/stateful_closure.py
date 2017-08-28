# write a class object to count missing items

from collections import defaultdict

class Counter(object):
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0

current = {'monkey' : 2, 'donkey' : 3}
increment = [('elephant', 1), ('monkey' , 3), ('cat' , 5)]

c = Counter()
d = defaultdict(c, current)
print(d)
for animal, amount in increment:
    d[animal] += amount
print(d)
print(c.added)
