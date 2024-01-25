N = 7
K = 3
L = 7
M = {}
smPrime = float('inf')

def match(num, regex, dig, how_often, start_pos):
    global smPrime
    as_dig = str(dig)
    for i in range(start_pos, N):
        if regex[i] != as_dig:
            continue
        if i == 0 and as_dig == '0':
            continue
        regex[i] = '.'
        if how_often == 1:
            add_to = M.setdefault("".join(regex), [])
            add_to.append(num)
            if len(add_to) >= L and add_to[0] < smPrime:
                smPrime = add_to[0]
        else:
            match(num, regex, dig, how_often - 1, i + 1)
        regex[i] = as_dig

def main():
    global N, K, L, smPrime
    N, K, L = map(int, input().split())

    min_num = 1
    for i in range(1, N):
        min_num *= 10
    max_num = min_num * 10 - 1
    primes = [True] * (max_num + 1)
    primes[0], primes[1] = False, False

    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for j in range(2 * i, max_num + 1, i):
                primes[j] = False

    for i in range(min_num, max_num + 1):
        if primes[i]:
            str_num = str(i)
            for dig in range(10):
                match(i, list(str_num), dig, K, 0)
            if N == 7:
                if K == 1 and i > 2 * 10 ** 6:
                    break
                if K == 2 and i > 3 * 10 ** 6:
                    break

    mini = ""
    for key, values in M.items():
        if len(values) < L:
            continue
        if values[0] != smPrime:
            continue
        s = " ".join(map(str, values[:L]))
        if mini > s or not mini:
            mini = s
    print(mini)

if __name__ == "__main__":
    main()
