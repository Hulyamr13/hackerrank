from array import array
from bisect import bisect_right


def insertionSort(arr):
    shifts = 0
    n = len(arr)
    sarr = array('I', [arr[0]])
    for i in range(1, n):
        e = arr[i]
        j = bisect_right(sarr, e)
        sarr.insert(j, e)
        shifts += i - j
    return shifts


if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = insertionSort(arr)
        print(result)