def maxMin(k, arr):
    arr.sort() # Sort the array in ascending order
    min_unfairness = float('inf') # Initialize minimum unfairness to positive infinity

    # Iterate through the array and calculate unfairness for each subarray of length k
    for i in range(len(arr) - k + 1):
        unfairness = arr[i + k - 1] - arr[i] # Calculate unfairness for current subarray
        min_unfairness = min(min_unfairness, unfairness) # Update minimum unfairness

    return min_unfairness

if __name__ == '__main__':
    n = int(input().strip())
    k = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)
    result = maxMin(k, arr)
    print(result)
