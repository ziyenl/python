phrase_one = "The dog jump over the fox and the fence."

phrase_two = "The monkey" \
          "plays with the dog" \
          "today and tomorrow"

def find_index(phrase):
    index_list = [0,]
    for index, c in enumerate(phrase):
        if c == ' ':
            index_list.append(index+1)
    return index_list


def find_index_generator(phrase):
    if phrase:
        yield 0
    for index, c in enumerate(phrase):
        if c == ' ':
            yield index + 1

handle = open('phrase.txt')

def stream_from_file(handle):
    for line in handle:
        if line:
            ite = 0
            yield ite
            for i in line:
                ite = ite + 1
                if i == ' ':
                    yield ite


a = stream_from_file(handle)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
