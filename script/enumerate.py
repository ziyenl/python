__author__ = 'ziyenl'

# when you need an index of a list use enumerate generator
animals = ['dog', 'cat', 'bear', 'tiger']

for animal in enumerate(animals, 1):
    print(animal)
