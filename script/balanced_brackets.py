# This is solution to the balanced brackets problem
# https://www.hackerrank.com/challenges/ctci-balanced-brackets
def is_matched(expression):
    ''' check if expression matches '''
    stack = []
    mapping = { '{' : '}', '[' : ']', '(' : ')'}
  
    for expr in expression:
        if expr in mapping.keys():
            stack.append(mapping[expr])
        else:
            if len(stack) == 0 or stack.pop() <> expr:
                return False
    if len(stack) <> 0: return False
    return True

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
