class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'
    
class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, value):
        new_node = Node(value)

        new_node.next = self.top
        self.top = new_node

        self.length += 1


    def pop(self):
        assert self.top, "Stack is emtpy!"
        temp = self.top.val
        self.top = self.top.next
        self.length -= 1

        return temp

    def peek(self):
        assert self.top, "Stack is empty!" # print if top is null
        return self.top.val

    def isEmpty(self):
        return self.length == 0

    def size(self):
        return self.length