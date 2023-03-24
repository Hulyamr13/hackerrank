def merge_the_tools(string, k):
    # Split the string into n/k substrings of length k
    substrings = [string[i:i + k] for i in range(0, len(string), k)]

    # Create subsequence for each substring and print it
    for substring in substrings:
        # Create a list to store unique characters in order of their first occurrence
        unique_chars = []
        for char in substring:
            # Add the character to the list if it is not already in the list
            if char not in unique_chars:
                unique_chars.append(char)

        # Print the subsequence
        print("".join(unique_chars))


if __name__ == '__main__':
    string = input().strip()
    k = int(input().strip())
    merge_the_tools(string, k)
