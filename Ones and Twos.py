MOD = 10**9 + 7
dp_sum = [[-1] * 1001 for _ in range(1001)]
dp_bit = [[-1] * 1001 for _ in range(1001)]

def add(x, v):
    global MOD
    v %= MOD
    x += v
    if x >= MOD:
        x -= MOD
    return x

def f_bit(lv, B):
    global dp_bit
    if lv > B:
        return 0
    if dp_bit[lv][B] != -1:
        return dp_bit[lv][B]
    return f_sum(lv + 1, B - lv)

def f_sum(lv, B):
    global dp_sum
    if lv > B:
        return 1
    if dp_sum[lv][B] != -1:
        return dp_sum[lv][B]
    tmp = f_sum(lv + 1, B)
    tmp = add(tmp, f_bit(lv, B))
    dp_sum[lv][B] = tmp
    return tmp

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        an = 0
        if A == 0:
            an = f_sum(1, B)
        else:
            k = 1
            while (1 << k) <= A:
                k += 1
            k += 1
            an = add(an, (A + 1) * f_sum(k, B))
            ha = (1 << k) - A - 1
            now = 0
            i = 1
            last = 0
            while ha > 0:
                now += 1
                if B < now:
                    break
                an = add(an, min((1 << i) - last, ha) * f_sum(k, B - now))
                ha -= (1 << i) - last
                last = 1 << i
                i += 1
                if i == k:
                    last = 0
                    i = 1
        print((an + MOD - 1) % MOD)
