class Node(object):
	''' Node of queue data structure '''
	def __init__(self, data, node=None):
		self.data = data
		self.next = node
	
class Queue(object):
	'''  Queue data structure '''
	def __init__(self):
		self._head = None
		self._tail = None
		
	def peek(self):
		''' get first element on queue '''
		return self._head.data
	
	def add(self, data):
		''' add node to queue '''
		new_node = Node(data)
		if self.isEmpty():
			self._head = self._tail = new_node
		else:
			self._tail.next = new_node
			self._tail = new_node
		
	def remove(self):
		''' remove node from queue '''
		if not self.isEmpty():
			return_data = self._head.data
			self._head = self._head.next
			if self._head is Nnone:
				self._tail = None
			
			return return_data
	
	def isEmpty(self):
		''' check if queue is empty '''
		return self._tail is None
