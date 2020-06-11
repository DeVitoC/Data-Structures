"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        prev_tail = self.storage.remove_from_tail()
        return prev_tail


# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
#
#     def __len__(self):
#         return self.size
#
#     def enqueue(self, value):
#         self.storage.insert(0, value)
#         self.size += 1
#
#     def dequeue(self):
#         if self.size == 0:
#             return None
#         self.size -= 1
#         return self.storage.pop()

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, data):
        new_node = Node(data)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            prev_head = self.head
            self.head = new_node
            self.head.set_next(prev_head)

    def remove_from_tail(self):
        if self.head is None: return None
        data = self.tail.get_data()
        if self.head != self.tail:

            self.tail = self.get_previous(self.tail)
            self.tail.next = None
        else:
            self.head = None
            self.tail = None
        return data

    def get_previous(self, node):
        if not self.head.get_next: return None
        num = 0
        temp_node = self.head
        while True:
            if temp_node.get_next() != None and temp_node.get_next() != node:
                num += 1
                temp_node = temp_node.get_next()
            else:
                return temp_node