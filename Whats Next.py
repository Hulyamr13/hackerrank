def modify_array(A):
    # Function to modify the array A as per the given conditions

    n = len(A)
    if n > 1:
        if n % 2 == 0:
            if n >= 4:
                if A[n - 3] == 1:
                    if A[n - 2] != 1:
                        A[n - 2] -= 1
                        A[n - 4] += 1
                        A[n - 3] += A[n - 1]
                        del A[n - 1]
                    else:
                        A[n - 4] += 1
                        A[n - 3] += A[n - 1]
                        del A[n - 2]
                        del A[n - 2]
                else:
                    A[n - 3] -= 1
                    A[n - 2] -= 1
                    for _ in range(2):
                        A.insert(n - 2, 1)
                    A[n - 1] += A[n + 1]
                    del A[n + 1]
            else:
                if A[n - 2] == 1:
                    A[n - 1] += 1
                else:
                    A = [1, A[n - 1] + 1, A[n - 2] - 1]

        else:
            if A[n - 2] == 1:
                if A[n - 1] != 1:
                    A[n - 1] -= 1
                    A[n - 3] += 1
                else:
                    A[n - 3] += 1
                    del A[n - 1]
            else:
                A[n - 2] -= 1
                A[n - 1] -= 1
                for _ in range(2):
                    A.insert(n - 1, 1)
    else:
        A[0] -= 1
        for _ in range(2):
            A.insert(0, 1)

    if A[-1] == 0:
        del A[-1]

    return A


def main():
    # Main function to take input and print output

    T = int(input().strip())  # Number of test cases
    for _ in range(T):
        binary_A = []
        n = int(input().strip())
        A = list(map(int, input().strip().split()))
        modified_A = modify_array(A)
        print(len(modified_A))
        print(' '.join(str(x) for x in modified_A))


if __name__ == '__main__':
    main()