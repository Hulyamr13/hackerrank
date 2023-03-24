def merge_the_tools(s, k):
    # Split string s into n/k substrings of length k
    substrings = [s[i:i + k] for i in range(0, len(s), k)]

    # Create subsequence for each substring
    for substring in substrings:
        # Create set of distinct characters in the substring
        distinct_chars = set(substring)

        # Join characters in set together to form subsequence
        subsequence = ''.join(distinct_chars)

        # Print subsequence
        print(subsequence)
