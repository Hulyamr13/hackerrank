def split_and_join(line):
    # split the line into a list of words
    words = line.split()

    # join the words using a hyphen and return the resulting string
    return '-'.join(words)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)