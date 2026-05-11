

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        assert self.items, 'No items!'
        return self.items.pop()

    def peek(self):
        assert self.items, 'No items!'
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def test():
    stk = Stack()
    stk.push(10)
    stk.push(20)
    stk.push(30)
    print(stk.peek())   # 30
    stk.push(40)
    print(stk.peek())   # 40

    while not stk.isEmpty():
        print(stk.pop(), end=' ')
    # 40 30 20 10

def builtin1():

    # For threaded programming
    from queue import LifoQueue

    stk = LifoQueue(maxsize=6)

    stk.put(10)
    stk.put(20)
    stk.put(30)
    #print(stk.peek())
    stk.put(40)

    print(stk.qsize())  # 4

    while not stk.empty():
        print(stk.get(), end=' ')
    # 40 30 20 10

    # Future Question:
    # What happens if we inserted more than 6?

if __name__ == '__main__':
    test()
