
class Queue:
    def __init__(self, size):
        self.added_elements = 0
        self.rear = self.front = 0
        # Let's use list to express our FIXED array
        self.array = [None] * max(1, size)

    def _next(self, pos):
        pos += 1
        if pos == len(self.array):
            pos = 0
        return pos
    # return (pos + 1) % size	#  Or shorter way

    def enqueue(self, value):
        assert not self.full()
        self.array[self.rear] = value
        self.rear = self._next(self.rear)
        self.added_elements += 1

    def dequeue(self):
        assert not self.empty()
        value = self.array[self.front]
        self.front = self._next(self.front)
        self.added_elements -= 1
        return value

    def empty(self):
        return self.added_elements == 0

    def full(self):
        return self.added_elements == len(self.array)

    def display(self):
        print(f"Front {self.front} - rear {self.rear}", end = '\t')

        if self.full():
            print("FULL", end='')
        elif self.empty():
            print("EMPTY\n")
            return

        print("")
        cur = self.front

        for step in range(self.added_elements):
            print(self.array[cur], end=" ")
            cur = self._next(cur)
        print("")


if __name__ == '__main__':

    qu = Queue(6)

    assert qu.empty()
    qu.display()

    for i in range(1, 7):
        assert not qu.full()
        qu.enqueue(i)
        qu.display()

    print()

    assert qu.full()
    for i in range(1, 7):
        assert not qu.empty()
        qu.dequeue()
        qu.display()

    print()

    for i in range(1, 7):
        assert not qu.full()
        qu.enqueue(i)
        qu.display()

    print()
    qu.dequeue()
    assert not qu.full()
    qu.enqueue(7)
    assert qu.full()
    qu.display()

    qu.dequeue()
    qu.dequeue()
    assert not qu.full()
    qu.enqueue(8)
    assert not qu.full()
    qu.display()
    qu.enqueue(9)
    assert qu.full()
    qu.display()

    assert qu.full()
    for i in range(1, 7):
        assert not qu.empty()
        qu.dequeue()
        qu.display()

'''

Front 0 - rear 0	EMPTY

Front 0 - rear 1	
1 
Front 0 - rear 2	
1 2 
Front 0 - rear 3	
1 2 3 
Front 0 - rear 4	
1 2 3 4 
Front 0 - rear 5	
1 2 3 4 5 
Front 0 - rear 0	FULL
1 2 3 4 5 6 

Front 1 - rear 0	
2 3 4 5 6 
Front 2 - rear 0	
3 4 5 6 
Front 3 - rear 0	
4 5 6 
Front 4 - rear 0	
5 6 
Front 5 - rear 0	
6 
Front 0 - rear 0	EMPTY


Front 0 - rear 1	
1 
Front 0 - rear 2	
1 2 
Front 0 - rear 3	
1 2 3 
Front 0 - rear 4	
1 2 3 4 
Front 0 - rear 5	
1 2 3 4 5 
Front 0 - rear 0	FULL
1 2 3 4 5 6 

Front 1 - rear 1	FULL
2 3 4 5 6 7 
Front 3 - rear 2	
4 5 6 7 8 
Front 3 - rear 3	FULL
4 5 6 7 8 9 
Front 4 - rear 3	
5 6 7 8 9 
Front 5 - rear 3	
6 7 8 9 
Front 0 - rear 3	
7 8 9 
Front 1 - rear 3	
8 9 
Front 2 - rear 3	
9 
Front 3 - rear 3	EMPTY
'''
