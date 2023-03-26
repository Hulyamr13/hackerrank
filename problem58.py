import itertools

n = int(input())
lst = input().split()
k = int(input())

# count total number of ways to select k indices out of n
total = len(list(itertools.combinations(range(n), k)))

# count number of ways to select k indices that do contain 'a'
num_with_a = len(list(filter(lambda x: 'a' in [lst[i] for i in x], itertools.combinations(range(n), k))))

# calculate probability and print
print('{:.4f}'.format(num_with_a / total))