t = int(input())  # number of test cases

for i in range(t):
    n = int(input())  # number of elements in set A
    A = set(map(int, input().split()))  # set A
    m = int(input())  # number of elements in set B
    B = set(map(int, input().split()))  # set B

    if A.issubset(B):
        print("True")
    else:
        print("False")