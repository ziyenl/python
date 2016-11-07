# This is solution for summing two linked list
# Problem described here: https://www.kancloud.cn/kancloud/data-structure-and-algorithm-notes/73006
# and http://www.geeksforgeeks.org/add-two-numbers-represented-by-linked-lists/
class Node(object):
	''' Node object '''
	def __init__(self, data=0):
		self.data = data
		self.next = None
 
class LinkedList(object):
	''' Linked List object '''
	def __init__(self):
		self._head_node = None
		
	def push(self, data):
		''' push data into linked list '''
		node = Node(data=data)
		node.next = self._head_node
		self._head_node = node
		
	def print_list( self ):
		''' print linked list '''
		start = self._head_node
		output = ''
		while(start):
			output += str(start.data) 
			if start and start.next:
				output +=  '->'
			start = start.next
		return output
		
	@classmethod
	def sum_list( cls, first_list, second_list ):
		''' Generate a sum list from two list provided '''
		increment_next = False
		summation = []
		first_node = first_list._head_node 
		second_node = second_list._head_node 
		
		while(first_node or second_node):
			total = 0 
			if first_node:
				total += first_node.data
				first_node = first_node.next 
			if second_node:
				total += second_node.data
				second_node = second_node.next
			if increment_next == True:
				total += 1
				increment_next = False
			if total > 9:
				total -= 10
				increment_next = True
			summation.append(total)
		return cls.generate_new_list(summation)
			
	@staticmethod
	def generate_new_list(summation, reverse=True):
		''' Generate a new list for a give array summation '''
		new_list = LinkedList()
		if reverse:
			summation = list(reversed(summation))
		for item in summation:
			new_list.push(item)
		return new_list
								
		
# Create two lists
first = LinkedList()
second = LinkedList()
  
 # First List
first.push(6)
first.push(4)
first.push(9)
first.push(5)
first.push(7)
print "First List: %s" % first.print_list()
 
# Second Llist
second.push(4)
second.push(8)
print "Second List: %s" % second.print_list()
	 
new_list = LinkedList.sum_list(first, second)
print "Sum List: %s" % new_list.print_list()
