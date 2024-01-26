end_palindromes = []

def is_palindrome(x):
    x = str(x)
    return x == x[::-1]

n = int(input())

for i in range(1, n + 1):
    iteration = 0
    while iteration < 60:
        if is_palindrome(i):
            end_palindromes.append(i)
            break
        i += int(str(i)[::-1])
        iteration += 1

max_count = 0
for i in sorted(set(end_palindromes)):
    y = end_palindromes.count(i)
    if y > max_count:
        answer = i
        max_count = y

print(answer, max_count)
