from collections import deque

q = deque()

q.append(3)  # enqueue O(1)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)

print("Peek:", q[0]) # peek is the front (first added item)

# it is pop left because the new appended ones are added to the right,
# and in q we want to dequeue the old elements (first in first out)

print(q.popleft())  # dequeue  O(1)
print(q) 
print(q.popleft())
print(q)
print(q.popleft())
print(q)

# we don't use normal lists, because the popping from the front is O(n) 
# since everything shifts

# you can also do append left then normal pop, dequeue is optimized
# so that both ends result in an O(1) time.

