# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def perf_arc(n):
    root = int(math.sqrt(n))
    if root * root == n:
        return 0
    a = 1
    listaint = [root]
    den = n - root * root
    lista_inv_frac = [(math.sqrt(n) + root) / den]
    per = 0
    while True:
        part_int = int(lista_inv_frac[-1])
        root = (den * part_int) // a - root
        a = den // a
        den = n - root * root
        invfrac = a * (math.sqrt(n) + root) / den
        listaint.append(part_int)
        lista_inv_frac.append(invfrac)
        per += 1
        if invfrac == lista_inv_frac[0]:
            return per

if __name__ == "__main__":
    n = int(input().strip())
    cnt_odd = 0
    for k in range(2, n + 1):
        if perf_arc(k) % 2 == 1:
            cnt_odd += 1

    print(cnt_odd)
