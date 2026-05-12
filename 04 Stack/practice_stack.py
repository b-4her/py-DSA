class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):  # O(1) amortized
        self.items.append(item)

    def pop(self):
        assert self.items, "Stack is emtpy!"
        return self.items.pop()

    def peek(self):
        assert self.items, "Stack is emtpy!"
        return self.items[-1]

    def isEmpty(self):
        return self.items

    def size(self):
        return len(self.items)


