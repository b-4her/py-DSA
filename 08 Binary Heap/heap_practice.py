
# for max heap, just multiply by -1 before insertion and mutiply by the -1 again after retreival
class BinaryMinHeap:
    def __init__(self):
        self.arr: list[int] = []

    def _get_parent(self, idx):
        return (idx - 1) // 2

    def _left_child(self, idx):
        return 2*idx + 1

    def _right_child(self, idx):
        return 2*idx + 2    

    # O(log(n)) = O(h)
    def _heapify_down(self, idx):  # fix heap
        left_idx = self._left_child(idx)
        right_idx = self._right_child(idx)

        min_idx = idx
        if left_idx < len(self.arr):  # has left
            if self.arr[left_idx] < self.arr[min_idx]:
                min_idx = left_idx

        if right_idx < len(self.arr):  # has right
            if self.arr[right_idx] < self.arr[min_idx]:
                min_idx = right_idx

        if min_idx != idx: # swap and fix
            cur = self.arr[idx]
            self.arr[idx] = self.arr[min_idx]
            self.arr[min_idx] = cur
            self._heapify_down(min_idx)

        # else; top is already the min, no need to fix anything!

    # O(log(n)) = O(h)
    def _heapify_up(self, idx):  # fix heap
        if idx == 0: # no more to do
            return
        
        parent_idx = self._get_parent(idx)

        cur = self.arr[idx]
        parent = self.arr[parent_idx]

        if cur < parent:
            # swap
            self.arr[idx] = parent
            self.arr[parent_idx] = cur
            self._heapify_up(parent_idx)

        # else, done! (already structured properly)

    # O(log(n)) = O(h)
    def insert(self, val):
        self.arr.append(val)
        self._heapify_up(len(self.arr)-1) # fix

    # O(log(n)) = O(h)
    def pop(self):
        assert not self.is_empty()
        min_val = self.arr[0]
        
        temp = self.arr.pop()
        if len(self.arr) > 0:
            self.arr[0] = temp
            self._heapify_down(0) # fix

        return min_val

    # O(n) -> see proof in notes (Floyd)
    def build_heap(self, lst):
        self.arr = lst[:]  # create a copy
        
        # len(self.arr) // 2 - 1 -> (first parent index)
        for i in range(len(self.arr) // 2 - 1, -1, -1): # iterate right half (parents) bottom up
            self._heapify_down(i)
            # ignore the second half of the arr (all leafs) -> heafipy down will do nothing for them!
    
    # notice that if we do normal insertion we get the complexity to be nlogn due to the heapify up

    # O(1) -> returns min
    def top(self):
        assert not self.is_empty()
        return self.arr[0]
    
    def is_empty(self):
        return len(self.arr) == 0

# O(n + nlog(n)) = O(nlog(n)) 
def heapSort(lst):
    heap = BinaryMinHeap()
    heap.build_heap(lst)

    sorted = []
    while not heap.is_empty():
        sorted.append(heap.pop())

    return sorted

if __name__ == "__main__":
    # Basic insert + top test
    heap = BinaryMinHeap()

    heap.insert(5)
    assert heap.top() == 5

    heap.insert(3)
    assert heap.top() == 3

    heap.insert(8)
    assert heap.top() == 3

    heap.insert(1)
    assert heap.top() == 1

    print("Insert/top tests passed")

    # Pop order test
    result = []
    while not heap.is_empty():
        result.append(heap.pop())

    assert result == [1, 3, 5, 8]
    print("Pop order test passed")

    # Heap sort tests
    assert heapSort([5, 3, 8, 1]) == [1, 3, 5, 8]
    assert heapSort([10, -1, 4, 0, 2]) == [-1, 0, 2, 4, 10]
    assert heapSort([1]) == [1]
    assert heapSort([]) == []
    assert heapSort([3, 3, 2, 1, 2]) == [1, 2, 2, 3, 3]

    print("Heap sort tests passed")

    # Mixed operations
    heap = BinaryMinHeap()

    heap.insert(20)
    heap.insert(15)
    heap.insert(30)
    heap.insert(5)

    assert heap.pop() == 5
    assert heap.top() == 15

    heap.insert(2)
    assert heap.top() == 2

    assert heap.pop() == 2
    assert heap.pop() == 15
    assert heap.pop() == 20
    assert heap.pop() == 30
    assert heap.is_empty()

    print("Mixed operation tests passed")

    print("ALL TESTS PASSED")