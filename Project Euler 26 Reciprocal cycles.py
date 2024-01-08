# Enter your code here. Read input from STDIN. Print output to STDOUT

def length_of_cycle(N):
    visited = [0] * N
    length = 0
    dividend = 10
    while dividend != 0:
        dividend %= N
        if visited[dividend]:
            return length  # Cycle repeats!
        visited[dividend] = 1
        length += 1
        dividend *= 10
    return 0  # No recurring cycle


def main():
    answer = [0] * 10000
    longest_cycle = 3
    index_of_longest_cycle = 3
    for i in range(3, 10000):
        cycle_length = length_of_cycle(i)
        if cycle_length > longest_cycle:
            longest_cycle = cycle_length
            index_of_longest_cycle = i
        answer[i] = index_of_longest_cycle

    num_test_cases = int(input())
    test_cases = [int(input()) for _ in range(num_test_cases)]

    for N in test_cases:
        if N <= 0:
            break
        print(answer[N - 1])

if __name__ == "__main__":
    main()
