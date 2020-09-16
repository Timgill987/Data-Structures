"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack? Where using an array and performing these built in methods causes 
    the computer to keep creating and deleting whole arrays to perform the tasks.
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size
#         pass

#     def push(self, value):
#         self.size += 1
#         self.storage.insert(0, value) Can use .append instead of insert on the tail
#         pass

#     def pop(self):
#         if self.size > 0:
#             self.size = self.size - 1
#             return self.storage.pop(0) can pop without using a param.

from singly_linked_list import LinkedList

class Stack: #using the linked list and its functions to carry out stacking
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)
        pass

    def pop(self):
        if self.size > 0:
            self.size = self.size - 1
            return self.storage.remove_tail()