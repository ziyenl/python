# Generator in class is useful when you want you would like to iterate more than once over the generator


sample_list = [40, 55, 25]

def calculate_percentage():
    total = sum(sample_list)
    percentages = []
    for item in sample_list:
        percentage = item / total * 100
        percentages.append(percentage)
    return percentages

print(calculate_percentage())

def write_to_file( path, written_list ):
    with open(path, 'r+') as h:
        for item in written_list:
            h.write(str(item) + '\n')

#write_to_file('num_list.txt', sample_list)

class CalculatePercentages(object):
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        with open(self.path, 'r+') as handle:
            for line in handle:
                yield int(line.strip())

def calculate_percentage_with_class(c):
    total = sum(c)
    for item in c:
        percentage = item / total * 100
        yield percentage

c = CalculatePercentages('num_list.txt')
print(list(calculate_percentage_with_class(c)))
ite = iter(c)
ite2 = iter(ite)
ite3 = iter(c)
assert ite == ite2
assert ite3 is not ite
