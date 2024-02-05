# Enter your code here. Read input from STDIN. Print output to STDOUT

def convert_to_base(num, base):
    res = 0
    digits = 0

    while num > 0:
        res += num % base
        digits += 1
        num //= base

    return res if digits >= 2 else -1

B = int(input())
ans = set()
limit = 999 if B <= 10 else (B * 50)

for i in range(2, limit + 1):
    p = i * i

    while p < 10**100:
        if p < B:
            p *= i
            continue
        digit_sum = convert_to_base(p, B)

        if digit_sum == i:
            ans.add(p)
        p *= i

output = sorted(list(ans))
print(" ".join(map(str, output)))
