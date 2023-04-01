import os


def chocolateFeast(n, c, m):
    # Compute initial number of chocolates
    num_chocolates = n // c
    # Initialize variables
    total_chocolates = num_chocolates
    wrappers = num_chocolates
    # While Bobby has enough wrappers to turn in for another chocolate bar
    while wrappers >= m:
        # Compute additional chocolates
        additional_chocolates = wrappers // m
        # Update total chocolates and wrappers
        total_chocolates += additional_chocolates
        wrappers = wrappers % m + additional_chocolates
    return total_chocolates


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        c = int(first_multiple_input[1])
        m = int(first_multiple_input[2])
        result = chocolateFeast(n, c, m)
        fptr.write(str(result) + '\n')
    fptr.close()
