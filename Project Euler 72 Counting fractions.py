# Enter your code here. Read input from STDIN. Print output to STDOUT

def compute_totient(limit):
    lookup = [i for i in range(limit + 1)]
    for i in range(2, limit + 1):
        if lookup[i] == i:
            for j in range(i, limit + 1, i):
                lookup[j] -= lookup[j] // i
    for i in range(3, limit):
        lookup[i] += lookup[i - 1]
    return lookup

def main():
    limit = 10**6
    lookup = compute_totient(limit)
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(lookup[n])

if __name__ == "__main__":
    main()
