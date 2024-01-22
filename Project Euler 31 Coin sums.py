# Enter your code here. Read input from STDIN. Print output to STDOUT

MOD = 10**9 + 7

def calculate_combinations(limit, multiples):
    lis = [0] * (limit + 1)
    lis[0] = 1

    for i in multiples:
        for n in range(limit - i + 1):
            lis[n + i] = (lis[n + i] + lis[n]) % MOD

    return lis

no = 10**5
multiples = [1, 2, 5, 10, 20, 50, 100, 200]

lis = calculate_combinations(no, multiples)

for _ in range(int(input())):
    n = int(input())
    print(lis[n] % MOD)
