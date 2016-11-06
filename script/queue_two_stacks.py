# This is solution for tales of two stacks
# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks
class MyQueue(object):
    def __init__(self):
        self.stack = []
    
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[0]
        
    def pop(self):
        item = self.stack[0]
        self.stack = self.stack[1:]
        return item
        
    def put(self, value):
        self.stack.append( value )
        

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
        
