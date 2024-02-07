# Enter your code here. Read input from STDIN. Print output to STDOUT

limit = 8000001
solutions = [0] * limit
for a in range(1, limit):
    for b in range((a + 3) // 4, a):
        current = a * (4 * b - a)
        if current >= limit:
            break
        solutions[current] += 1


tests = int(input())
for _ in range(tests):
    pos = int(input())
    print(solutions[pos])
