def max_subarray(t, arr):
    """
    Function to find the maximum subarray sum and subsequence sum for each test case.

    Args:
    - t: int, the number of test cases.
    - arr: list of lists of integers, the input arrays for each test case.

    Returns:
    - list of tuples of two integers, [(maximum subarray sum, subsequence sum), ...].
    """
    results = []
    for i in range(t):
        current_sum = best_start_ind = best_end_ind = current_ind = best_sum = 0
        ans = 0
        ans2 = 0
        min_val = -10000000
        count = 0

        n = len(arr[i])

        for k in range(n):
            if arr[i][k] < 0:
                count += 1
                if arr[i][k] > min_val:
                    min_val = arr[i][k]

            if arr[i][k] > 0:
                ans2 += arr[i][k]

            val = current_sum + arr[i][k]
            if val > 0:
                if current_sum == 0:
                    current_ind = k
                current_sum = val
            else:
                current_sum = 0

            if current_sum > best_sum:
                best_sum = current_sum
                best_start_ind = current_ind
                best_end_ind = k

        if count != n:
            for j in range(best_start_ind, best_end_ind + 1):
                ans += arr[i][j]
        else:
            ans = ans2 = min_val

        results.append((ans, ans2))

    return results


if __name__ == "__main__":
    t = int(input())  # Number of test cases
    arr = []
    for i in range(t):
        n = int(input())  # Input n
        arr.append(list(map(int, input().split())))  # Input array

    results = max_subarray(t, arr)

    for result in results:
        print(result[0], result[1])
