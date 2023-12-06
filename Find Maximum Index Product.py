n = int(input())
a = list(map(int, input().split()))
a.insert(0, None)
left = {}
right = {}
left[1] = 0
right[n] = 0
for i in range(2, n + 1):
    if a[i] == a[i - 1]:
        left[i] = left[i - 1]

    elif a[i] < a[i - 1]:
        left[i] = i - 1

    else:
        if left[i - 1] == 0:
            left[i] = 0
        else:
            counter = i - 1

            while True:
                leftNumber = a[left[counter]]

                if left[counter] == 1:
                    if a[1] > a[i]:
                        left[i] = 1
                    else:
                        left[i] = 0
                    break

                if leftNumber == a[i]:
                    left[i] = left[left[counter]]
                    break

                elif leftNumber > a[i]:
                    left[i] = left[counter]
                    break

                else:
                    if left[left[counter]] == 0:
                        left[i] = 0
                        break
                    else:
                        counter = left[counter]

for i in range(n - 1, 0, -1):
    if a[i] == a[i + 1]:
        right[i] = right[i + 1]

    elif a[i] < a[i + 1]:
        right[i] = i + 1

    else:
        if right[i + 1] == 0:
            right[i] = 0
        else:
            counter = i + 1

            while True:
                rightNumber = a[right[counter]]

                if right[counter] == n:
                    if a[n] > a[i]:
                        right[i] = n
                    else:
                        right[i] = 0
                    break

                if rightNumber == a[i]:
                    right[i] = right[right[counter]]
                    break

                elif rightNumber > a[i]:
                    right[i] = right[counter]
                    break

                else:
                    if right[right[counter]] == 0:
                        right[i] = 0
                        break
                    else:
                        counter = right[counter]

maxProduct = 0

for i in range(1, n):
    product = left[i] * right[i]

    if maxProduct < product:
        maxProduct = product

print(maxProduct)