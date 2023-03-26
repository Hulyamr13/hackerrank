def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    lines = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        lines.append((s[::-1]+s[1:]).center(4*size-3, "-"))
    print('\n'.join(lines[:0:-1]+lines))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)