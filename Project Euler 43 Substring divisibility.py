# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

nums = [2, 3, 5, 7, 11, 13, 17]
sums = [0] * 10

def is_strange(s):
    y = len(s)
    for i in range(1, y - 2):
        p = int(s[i:i+3])
        if p % nums[i - 1] != 0:
            return False
    return True

ss = [str(i) for i in range(10)]
s = "012"

for i in range(3, 10):
    s += ss[i]
    if is_strange(s):
        p = s if s[0] != '0' else s[1:]
        sums[i] += int(p)

    for perm in permutations(s):
        s_perm = ''.join(perm)
        if is_strange(s_perm):
            p = s_perm if s_perm[0] != '0' else s_perm[1:]
            sums[i] += int(p)

n = int(input())
print(sums[n])
