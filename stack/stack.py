"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""
import datetime


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        if not self.storage.head and not self.storage.tail: return 0
        num = 0
        node = self.storage.head
        while True:
            if node.get_next() != None:
                num += 1
                node = node.get_next()
            else:
                num += 1
                break
        return num

    def push(self, value):
        start = datetime.datetime.now()
        self.storage.add_to_tail(value)
        end = datetime.datetime.now()
        print(f"Push took {end - start} seonds")

    def pop(self):
        start = datetime.datetime.now()
        if len(self) >= 1:
            popped = self.storage.remove_from_tail()
            end = datetime.datetime.now()
            print(f"Pop took {end - start} seonds")
            return popped
        else:
            return None

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

    def add_to_tail(self, data):
        new_node = Node(data)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

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

# stack = Stack()
