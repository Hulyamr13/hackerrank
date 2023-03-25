from collections import deque

d = deque()

# Get the number of operations to perform
n = int(input())

# Perform the operations
for i in range(n):
    operation = input().split()
    if operation[0] == 'append':
        d.append(operation[1])
    elif operation[0] == 'appendleft':
        d.appendleft(operation[1])
    elif operation[0] == 'pop':
        d.pop()
    elif operation[0] == 'popleft':
        d.popleft()

# Print the deque
print(' '.join(d))
