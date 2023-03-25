n = int(input())
word_counts = {}
word_order = {}
for i in range(n):
    word = input().strip()
    if word not in word_counts:
        word_counts[word] = 0
        word_order[word] = i
    word_counts[word] += 1

# Sort the words by their order of appearance
sorted_words = sorted(word_counts.keys(), key=lambda w: word_order[w])

# Output the number of distinct words and their counts
print(len(sorted_words))
for word in sorted_words:
    print(word_counts[word], end=" ")
print()
