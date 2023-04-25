def xor_sum(T, test_cases):
    # Function to calculate XOR sum for each test case

    results = []
    for i in range(T):
        N = test_cases[i][0]
        ar = test_cases[i][1]

        result = 0
        count = 0
        for i in range(N):
            count += N - 2*i
            if (count) % 2 == 1:
                result = result ^ ar[i]

        results.append(result)

    return results


if __name__ == '__main__':
    T = int(input())  # Number of test cases

    test_cases = []
    for _ in range(T):
        N = int(input())
        ar = [int(i) for i in input().split()]
        test_cases.append((N, ar))

    results = xor_sum(T, test_cases)

    for result in results:
        print(result)
