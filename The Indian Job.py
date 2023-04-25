
def parse_input():
    T = int(input())
    test_cases = []
    for t in range(T):
        N, G = map(int, input().split())
        A = [int(x) for x in input().split()]
        test_cases.append((N, G, A))
    return test_cases


def is_possible(N, G, A):
    s = set([0])
    for x in A:
        for t in list(s):
            s.add(x + t)
    x = sum(A)
    for t in s:
        if t <= G and x - t <= G:
            return 'YES'
    return 'NO'


def main():
    test_cases = parse_input()
    for N, G, A in test_cases:
        result = is_possible(N, G, A)
        print(result)


if __name__ == "__main__":
    main()
