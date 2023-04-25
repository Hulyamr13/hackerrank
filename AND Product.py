def and_product(start, end):
    # Function to calculate the AND product for a given range

    result = start
    steps = end - start
    i = 0
    while (start >> i) > 0:
        # If the number of steps causes the ith bit to flip, then
        # the result of that bit should be 0.
        if lmask(start, i + 1) + steps > lmask(-1, i + 1):
            result = bitmask(result, i)
        i += 1
    return result

def lmask(n, k):
    # Function to calculate the left mask of n for k bits

    return n & ((1 << k) - 1)

def bitmask(n, k):
    # Function to calculate the bit mask of n for k bits

    return n & ((-1 << (k + 1)) | lmask(-1, k))

def main():
    # Main function to take input and print output

    k = int(input())  # Number of test cases
    for _ in range(k):
        start, end = input().split()
        print(and_product(int(start), int(end)))

if __name__ == '__main__':
    main()