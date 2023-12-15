N = int(input())
heights = [int(x) for x in input().split()]

assert len(heights) == N

stack = []

result = 0

for h in heights:
    while len(stack) > 0 and stack[-1][0] < h:
        stack.pop()
    if len(stack) > 0 and stack[-1][0] == h:
        result += stack[-1][1]
        stack[-1] = (stack[-1][0], stack[-1][1] + 1)
    else:
        stack.append((h, 1))

print(2 * result)