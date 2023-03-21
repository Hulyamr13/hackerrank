if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    # Create a tuple from the integer_list
    t = tuple(integer_list)

    # Print the hash value of the tuple
    print(hash(t))