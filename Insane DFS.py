# Enter your code here. Read input from STDIN. Print output to STDOUT

MOD = 10**9 + 7
MAXN = 10**5
MAXAI = 200
factLim = 2 * MAXN + MAXAI

fact = [1] + [0] * (factLim)
for i in range(1, factLim + 1):
    fact[i] = fact[i - 1] * i % MOD

def comb(n, k):
    if k < 0 or n < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return fact[n] * pow(fact[k] * fact[n - k], MOD - 2, MOD) % MOD

def preliminary_check_is_invalid(S, N):
    if S[0] != "?" and S[0] != 0:
        return True
    for i in range(1, N):
        if S[i] != "?" and S[i] > i:
            return True
        if S[i] == 0:
            return True
        if (S[i] != "?" and S[i - 1] != "?") and S[i] - 1 > S[i - 1]:
            return True
    return False

def num_question_seq(a, b, n):
    return comb(2 * n + a - b + 1, n) - comb(2 * n + a - b + 1, n - b)

def num_suitable(S, N):
    if preliminary_check_is_invalid(S, N):
        return 0
    S[0] = 0
    S += [1]
    a_index = 0
    b_index = 1
    ans = 1

    while a_index < N and b_index < N:
        while b_index < N and S[b_index] == "?":
            b_index += 1
        n = b_index - a_index - 1
        a, b = S[a_index], S[b_index]
        if n > 0:
            ans = ans * num_question_seq(a, b, n) % MOD
        a_index = b_index
        b_index += 1

    return ans

N = int(input())
S = [int(k) if k.isdigit() else k for k in input().split()]
print(num_suitable(S, N))
