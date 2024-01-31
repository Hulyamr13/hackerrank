# Enter your code here. Read input from STDIN. Print output to STDOUT

memo = {}
pyramid = []
max_sum = -1


def slide(row, index):
    if row == len(pyramid):
        return 0
    if (row, index) not in memo:
        memo[(row, index)] = pyramid[row][index] + max(slide(row + 1, index), slide(row + 1, index + 1))
    return memo[(row, index)]


def main():
    global pyramid, memo, max_sum
    t = int(input())

    for _ in range(t):
        n = int(input())
        pyramid = []

        for i in range(n):
            pyramid.append(list(map(int, input().split())))

        print(slide(0, 0))
        memo = {}


if __name__ == "__main__":
    main()
