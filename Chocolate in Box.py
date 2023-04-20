def chocolateInBox(arr):
    xa = 0
    for x in arr:
        xa ^= x
    turns = sum(1 for x in arr if x ^ xa < x)
    return turns

if __name__ == '__main__':
    n = int(input()) # Number of containers
    a = [int(x) for x in input().split()] # Number of chocolates in each container
    result = chocolateInBox(a)
    print(result)