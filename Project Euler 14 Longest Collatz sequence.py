# Enter your code here. Read input from STDIN. Print output to STDOUT

MaxN = 5000000 + 2
cache = [-1] * MaxN

def steps(x):
    if x == 1:
        return 1

    if x < len(cache) and cache[x] != -1:
        return cache[x]

    if x % 2 == 0:
        next_val = x // 2
    else:
        next_val = 3 * x + 1

    result = 1 + steps(next_val)
    if x < len(cache):
        cache[x] = result

    return result

longest = {1: 1}

tests = int(input())
max_tested = 1
for _ in range(tests):
    x = int(input())

    while max_tested <= x:
        length = steps(max_tested)
        if length >= max(longest.values()):
            longest[max_tested] = length
        max_tested += 1

    best = max((k, v) for k, v in longest.items() if k <= x)
    print(best[0])