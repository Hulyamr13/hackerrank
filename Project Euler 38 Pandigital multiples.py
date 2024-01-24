# Enter your code here. Read input from STDIN. Print output to STDOUT

digits = {9: list('123456789'), 8: list('12345678')}
n, k = map(int, input().strip().split())

for i in range(2, n):
    value = i
    s = ''

    for j in range(1, k + 1):
        value = i * j
        s += str(value)

        if list(s) != list(dict.fromkeys(list(s))):
            break

        if sorted(list(s)) == digits[k]:
            print(i)
            break
