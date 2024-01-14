MOD = 1000000007

# Calculate factorials and their inverses modulo MOD
def calculate_factorials(n):
    factlist = [1]
    for i in range(1, n + 1):
        factlist.append((factlist[-1] * i) % MOD)
    return factlist

def calculate_inverse_factorials(factlist):
    factinvlist = [0] * len(factlist)
    factinvlist[-1] = pow(factlist[-1], MOD - 2, MOD)
    for i in range(len(factlist) - 1, 0, -1):
        factinvlist[i - 1] = (factinvlist[i] * i) % MOD
    return factinvlist

def binomial_coefficient(n, r, factlist, factinvlist):
    if n < r:
        return 0
    else:
        return (factlist[n] * factinvlist[r] * factinvlist[n - r]) % MOD

def count_beautiful_sets(q):
    factlist = calculate_factorials(2000000)
    factinvlist = calculate_inverse_factorials(factlist)

    for _ in range(q):
        n, k = map(int, input().split())
        if k == 0:
            print(1)
        else:
            toprint = 0
            for i in range(1, (k // 2) + 1):
                extra1s = k - 2 * i
                choice1s = binomial_coefficient(extra1s + i - 1, i - 1, factlist, factinvlist)
                extra0s = n - k - i + 1
                choice0s = binomial_coefficient(extra0s + i, i, factlist, factinvlist)
                toprint += choice1s * choice0s
            print(toprint % MOD)

if __name__ == "__main__":
    q = int(input())
    count_beautiful_sets(q)
