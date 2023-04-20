def insertionSort2(n, arr):
    for i in range(1, n):  # Start from the second element
        key = arr[i]  # Element to be inserted
        j = i - 1  # Index of the previous element

        # Compare the key with each previous element and shift them to the right if they are greater
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key  # Insert the key at its correct position
        print(*arr)  # Print the array after each iteration

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)