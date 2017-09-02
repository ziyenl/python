# https://www.hackerrank.com/challenges/recursive-digit-sum
# Algorithm:
# Do summation on the first half of the digit since it is of bigger dimension
# After summation of first half we multiple first half with second half and do summation on the result
# Worth noting of a solution of x * y % 9 based on mentioned http://applet-magic.com/digitsummod9.htm
# where summation of digit modulus 9 is equivalent to x * y % 9

def super_digit(p):
    if len(p) == 1:
        return p
    else:
        p = sum([int(p_item) for p_item in p])
        return super_digit(str(p))


if __name__ == '__main__':
    line = input()
    x, y = line.split(' ')
    first_digit_output = super_digit(x)
    second_digit_output = super_digit(first_digit_output * int(y))
    print(second_digit_output)
