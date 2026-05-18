# =========================================================
# PYTHON heapq SUMMARY
# =========================================================

import heapq


# =========================================================
# CREATE MIN HEAP
# =========================================================
# Python heapq is a MIN HEAP by default

heap = []


# =========================================================
# INSERT INTO HEAP
# =========================================================

heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)

# Heap structure internally:
# [2, 5, 8]
#
# Smallest element always at heap[0]


# =========================================================
# ACCESS MINIMUM ELEMENT
# =========================================================

minimum = heap[0]

print(minimum)   # 2


# =========================================================
# POP MINIMUM ELEMENT
# =========================================================

minimum = heapq.heappop(heap)

print(minimum)   # 2

# Heap is automatically restructured


# =========================================================
# BUILD HEAP FROM EXISTING ARRAY
# =========================================================
# Complexity: O(N)

arr = [5, 1, 8, 3]

heapq.heapify(arr)

print(arr)

# arr is now a valid min heap
# NOT necessarily sorted!


# =========================================================
# MAX HEAP TRICK
# =========================================================
# Multiply values by -1

max_heap = []

heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -8)

largest = -heapq.heappop(max_heap)

print(largest)   # 8


# =========================================================
# HEAP WITH TUPLES
# =========================================================
# Very common in interviews

heap = []

heapq.heappush(heap, (2, "task B"))
heapq.heappush(heap, (1, "task A"))
heapq.heappush(heap, (3, "task C"))

print(heapq.heappop(heap))

# (1, 'task A')
#
# Tuples are compared lexicographically


# =========================================================
# STABLE PRIORITY QUEUE TRICK
# =========================================================
# Preserve insertion order for same priorities

heap = []

timestamp = 0

heapq.heappush(heap, (2, timestamp, "A"))
timestamp += 1

heapq.heappush(heap, (2, timestamp, "B"))
timestamp += 1

print(heapq.heappop(heap))

# (2, 0, 'A')


# =========================================================
# PUSH + POP COMBINED
# =========================================================
# More efficient than:
# push then pop separately

heap = [2, 5, 8]
heapq.heapify(heap)

result = heapq.heappushpop(heap, 1)

print(result)   # 1


# =========================================================
# POP + PUSH COMBINED
# =========================================================

heap = [2, 5, 8]
heapq.heapify(heap)

result = heapq.heapreplace(heap, 10)

print(result)   # 2


# =========================================================
# KTH LARGEST ELEMENT PATTERN
# =========================================================
# Maintain min heap of size k

nums = [5, 1, 8, 3, 10]
k = 3

heap = []

for num in nums:

    heapq.heappush(heap, num)

    # keep only largest k elements
    if len(heap) > k:
        heapq.heappop(heap)

# kth largest
print(heap[0])   # 5


# =========================================================
# COMPLEXITIES
# =========================================================
#
# heappush     -> O(log N)
# heappop      -> O(log N)
# heapify      -> O(N)
# heap[0]      -> O(1)
#
#
# IMPORTANT:
# Heap is NOT fully sorted.
#
# Only guarantees:
#
# parent <= children
#
# for min heap.