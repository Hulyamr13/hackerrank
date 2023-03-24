from collections import defaultdict

n, m = map(int, input().split())

# Create a defaultdict to store the indices of each word in group A
indices = defaultdict(list)

# Read in the words belonging to group A and store their indices
for i in range(n):
    word = input().strip()
    indices[word].append(i+1)

# Check if each word in group B has appeared in group A
for i in range(m):
    word = input().strip()
    if word in indices:
        # If the word is in group A, print its indices
        print(" ".join(map(str, indices[word])))
    else:
        # If the word is not in group A, print -1
        print("-1")
