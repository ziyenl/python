# https://www.hackerrank.com/challenges/queue-using-two-stacks/problem

class Queue(object):
    def __init__(self):
        self._front = []
        self._back = []
        
    def queue(self, item):
        self._front.append(item)
        
    def dequeue(self):
        if len(self._back) > 0 or len(self._front) > 0:
            if self._back:
                    self._back = []
            else:
                self._front = self._front[1:]
            
    def peek(self):
        if self._front and not self._back:
            self._back.append(self._front[0])
            self._front = self._front[1:]
        return self._back[0]
         
if __name__ == '__main__':
    query = int(input())
    q = Queue()
    for idx in range(query):
        command = input()
        command = command.split(' ')
        # indicate query command
        if len(command) == 2 and command[0] == '1':
            q.queue(int(command[1]))
        if len(command) == 1 and command[0] == '2':
            q.dequeue()
        if len(command) == 1 and command[0] == '3':
            print(q.peek())
