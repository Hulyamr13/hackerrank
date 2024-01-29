from functools import lru_cache

@lru_cache(maxsize = None)
def s1(n):
    if n<3: return n
    if n%2==0: return s1(n//2) + s1(n//2-1) + n//2
    return 2*s1(n//2)+n//2+1

def s2(n):
    res = 0
    for i in range(1,40):
        if 2**i > n:
            return res + (s1(n) - s1(2**(i-1)-1)) / i
        res += (1+1/i)/2 * 2**(i-1)

for _ in range(int(input())):
    a,b = map(int,input().split())
    ans1 = (s2(b) - s2(a-1)) / (b-a+1)
    ans2 = (s1(b) - s1(a-1)) / (b-a+1)
    print("%.5f %.5f" % (ans1, ans2))