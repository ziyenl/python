# This is solution for tales of two stacks
# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks
class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
    
    def peek(self):
        ''' View first element of queue '''
        if len(self.first) > 0:
            return self.first[0]
        
    def pop(self):
        ''' Remove first element of the queue '''
        if len(self.first) > 0:
            self.second.append( self.first[0] )
            self.first = self.first[1:]
            return self.second.pop()
        
    def put(self, value):
        ''' Add element to queue '''
        self.first.append( value )
        

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
        
