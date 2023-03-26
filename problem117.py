x, k = map(int, input().split())
polynomial = input()

# Evaluate the polynomial
result = eval(polynomial)

# Check if result equals k
if result == k:
    print(True)
else:
    print(False)