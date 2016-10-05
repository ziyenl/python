__author__ = 'ziyenl'

# When you need to manipulate two list, use zip
# In Python 3.x, zip is a lazy generator that wraps 2 or more iterators that can be subsequently exhausted
# In Python 2.x, zip is not a lazy generator, therefore it is recommended to use izip
#Python 3.x
animals = ['dog', 'cat', 'bear', 'tiger']
animal_lengths = [ len(animal) for animal in animals ]
max_length = 0
for animal, length in zip( animals, animal_lengths ):
    if length > max_length:
        longest_animal = animal
print(longest_animal)

#Python 2.7x
from itertools import izip
animals = ['dog', 'cat', 'bear', 'tiger']
animal_lengths = [ len(animal) for animal in animals ]
max_length = 0
for animal, length in izip( animals, animal_lengths ):
    if length > max_length:
        longest_animal = animal
print(longest_animal)

#Both in order to prevent premature cut off of iterators length
from itertools import izip_longest
animals = ['dog', 'cat', 'bear', 'tiger']
animal_lengths = [ len(animal) for animal in animals ]
animals.append( 'donkey' )
max_length = 0
for animal, length in izip_longest( animals, animal_lengths ):
    if length > max_length:
        longest_animal = animal
print(longest_animal)
