stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print(stack[-1])   # 3 (access top)

while stack:
    print(stack.pop())