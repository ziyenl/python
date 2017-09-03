class Queue(object):
    
    def __init__(self):
        self._queue = []
        
    def queue(self, item):
        self._queue.append(item)
        
    def dequeue(self):
        if len(self._queue) > 0:
            self._queue = self._queue[1:]
            
    def peek(self):
        if len(self._queue) > 0:
            return self._queue[0]
         
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
