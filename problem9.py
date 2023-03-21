N = int(input())
lst = list(map(int, input().split()))

if all(x > 0 for x in lst):
    if any(str(x) == str(x)[::-1] for x in lst):
        print("True")
    else:
        print("False")
else:
    print("False")
