WORD_LIST = "sowpods.txt"
wordlist = open(WORD_LIST).readlines()
# Get rid of newlines
wordlist = [word.lower().strip() for word in wordlist]

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}

# list of words with double uus
a = filter(lambda x: 'uu'.upper() in x.upper(), wordlist)
#print(list(a))

# list of words without double characters
import string
letter = []
for alphabet in string.ascii_lowercase:
    double = alphabet * 2;
    has_double = False
    for word in wordlist:
        if double in word:
            has_double = True
            break
    if not has_double:
        letter.append(alphabet)
#print(letter)

def has_all_vowels(word):
    vowels = 'aeiou'
    for vowel in vowels:
        if vowel not in word:
            return False
    return True

def get_vowel_words():
    vowel_words = []
    for word in wordlist:
        if(has_all_vowels(word)):
            vowel_words.append(word)
    return vowel_words

from timeit import timeit
#print(timeit("get_vowel_words()", "from __main__ import wordlist, get_vowel_words, has_all_vowels"))

def is_word_palindrome(word):
    word_len = len(word)
    index = 0
    while index < int(word_len / 2):
        if word[index] != word[-(index+1)]:
            return False
        index = index + 1
    return True

#def get_longest_palindrome():
#    palindrome_list = []
#    for word in wordlist:
#        if is_word_palindrome(word):
#            palindrome_list.append(word)
#    max_length = max(map(lambda x: len(x), palindrome_list))
#    return list(filter(lambda x: len(x) == max_length, palindrome_list))

# better appoach
def get_longest_palindrome():
    longest = ''
    for word in wordlist:
        if word == word[::-1] and len(word) > len(longest):
            longest = word
    return longest

#from timeit import timeit
#print(timeit("get_longest_palindrome()", "from __main__ import  get_longest_palindrome, wordlist"))

def generate_sonnet():
    d = open('sonnet_words.txt').readlines();
    for a in d:
        yield a.strip()

all_sonnets = [ a.strip() for a in open('sonnet_words.txt').readlines()]
print(next(generate_sonnet()))
print(next(generate_sonnet()))
