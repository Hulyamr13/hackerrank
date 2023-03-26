from itertools import combinations_with_replacement

s, k = input().split()
k = int(k)

# Generate all combinations with replacement
combs = combinations_with_replacement(sorted(s), k)

# Print the combinations in lexicographic order
for comb in combs:
    print(''.join(comb))