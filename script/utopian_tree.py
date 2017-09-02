# https://www.hackerrank.com/challenges/utopian-tree
# Just have to be careful about how range works to check

def estimate_growth(cycles, height):
    if cycles == 0:
        return height
    for cycle in range(1, cycles+1):
        if cycle % 2 == 1:
            height *= 2 
        else:
            height += 1
    return height

if __name__ == '__main__':
    cases = int(input())
    for c in range(cases):
        case = int(input())
        print(estimate_growth(case, 1))
    
    
