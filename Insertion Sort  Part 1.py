def insertionSort1(n, arr):
    # Store the value of the unsorted number
    unsorted_num = arr[n - 1]

    # Start from the second-to-last element and move towards the beginning
    for i in range(n - 2, -1, -1):
        # If the current element is greater than the unsorted number
        if arr[i] > unsorted_num:
            # Shift the current element one position to the right
            arr[i + 1] = arr[i]
            # Print the interim array
            print(*arr)
        else:
            # Insert the unsorted number at the current position
            arr[i + 1] = unsorted_num
            # Print the interim array
            print(*arr)
            # Break out of the loop
            break
    else:
        # If the loop completes without finding the correct position,
        # insert the unsorted number at the beginning of the array
        arr[0] = unsorted_num
        # Print the interim array
        print(*arr)


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)
