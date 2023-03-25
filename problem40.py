from collections import Counter

if __name__ == '__main__':
    s = input()

    # count the frequency of each character
    freq = Counter(s)

    # sort the characters based on their frequency
    sorted_chars = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    # print the top three most common characters
    for char, count in sorted_chars[:3]:
        print(char, count)
