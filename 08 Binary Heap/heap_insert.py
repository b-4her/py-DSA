

class MinHeap:
    def __init__(self):
        self.array = []
        self.size = 0   # Actual number of elements

    def _left(self, node):
        p = 2 * node + 1
        if p >= self.size:
            return -1
        return p

    def _right(self, node):
        p = 2 * node + 2
        return -1 if p >= self.size else p

    def _parent(self, node):
        return -1 if node == 0 else (node - 1) // 2

    def _heapify_up(self, child_pos):
        # stop when parent is smaller or no parent
        par_pos = self._parent(child_pos)
        if child_pos == 0 or self.array[par_pos] < self.array[child_pos]:
            return
        # swap
        self.array[child_pos], self.array[par_pos] = \
            self.array[par_pos], self.array[child_pos]
        self._heapify_up(par_pos)

    def push(self, key):
        if self.size + 1 >= len(self.array):
            self.array.append(None)

        self.array[self.size] = key
        self.size += 1
        self._heapify_up(self.size - 1)

    def top(self):
        assert not self.empty()
        return self.array[0]

    def empty(self):
        return self.size == 0



# Driver Code
if __name__ == "__main__":
    minHeap = MinHeap()
    lst = [2, 17, 22, 10, 8, 37, 14, 19, 7, 6, 5, 12, 25, 30]

    for val in lst:
        minHeap.push(val)

    print(minHeap.array)
    # 2, 5, 12, 8, 6, 14, 22, 19, 17, 10, 7, 37, 25, 30

