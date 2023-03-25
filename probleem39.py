from collections import Counter

s = input()
count = Counter(s)

# Get the three most common characters
top_three = count.most_common(3)

# Sort in descending order of occurrence count
top_three = sorted(top_three, key=lambda x: (-x[1], x[0]))

# Print the result
for char, freq in top_three:
    print(char, freq)
