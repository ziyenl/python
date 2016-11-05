# This is solution to the left rotation in arrays
# https://www.hackerrank.com/challenges/ctci-linked-list-cycle
# Tortoise and Hare can be found at https://en.wikipedia.org/wiki/Cycle_detection
"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

# Storage method
def has_cycle(head):
    checked_list = []
    current_node = head
    while current_node:
        if current_node in checked_list:
            return True
        checked_list.append( current_node )
        current_node = current_node.next
    return False

# Floyd's cycle finding hare and tortoise
def has_cycle(head):
    if head is None: 
        return False
    tortoise = head 
    hare = head.next
    while(tortoise is not None and hare is not None and hare.next is not None):
        if tortoise == hare:
            return True
        tortoise = tortoise.next
        hare = hare.next.next
    return False
    
