from itertools import permutations

s, k = input().split()

# generate permutations and sort them lexicographically
perms = sorted(permutations(s, int(k)))

# print each permutation on a separate line
for p in perms:
    print(''.join(p))
