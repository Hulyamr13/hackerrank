def permutation():
    n = int(input())
    values = list(map(int, input().split()))

    output_values = [values[values[i] - 1] for i in range(n)]
    for val in output_values:
        print(val)

permutation()
