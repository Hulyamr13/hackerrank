def reverse_binary_sum(q, queries):
    # Function to calculate the sum of reverse binary numbers

    results = []
    for x in queries:
        binary = list(bin(x))[2:]
        binary.reverse()
        summ = 0
        for idx, item in enumerate(binary):
            if item == "0":
                summ += 2**idx

        results.append(summ)

    return results


if __name__ == '__main__':
    q = int(input().strip())  # Number of queries

    queries = []
    for _ in range(q):
        x = int(input().strip())
        queries.append(x)

    results = reverse_binary_sum(q, queries)

    for result in results:
        print(result)