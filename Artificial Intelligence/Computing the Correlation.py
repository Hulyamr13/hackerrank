# Enter your code here. Read input from STDIN. Print output to STDOUT


import math

def Std(l, mean, n):
    s = 0
    for i in range(n):
        s += (l[i] - mean) ** 2
    return math.sqrt(s / (n - 1))

def Correlation(a, b, n, s1, s2, meana, meanb):
    r = 0
    for i in range(n):
        r += (a[i] - meana) * (b[i] - meanb)
    return r / ((n - 1) * s1 * s2)

math_scores = []
phy_scores = []
chem_scores = []
mean_math = 0
mean_phy = 0
mean_chem = 0

n = int(input())
for i in range(n):
    m, p, c = map(int, input().split())
    mean_math += m
    mean_phy += p
    mean_chem += c
    math_scores.append(m)
    phy_scores.append(p)
    chem_scores.append(c)

mean_math /= n
mean_phy /= n
mean_chem /= n

sp = Std(phy_scores, mean_phy, n)
sm = Std(math_scores, mean_math, n)
sc = Std(chem_scores, mean_chem, n)

mp = Correlation(math_scores, phy_scores, n, sp, sm, mean_math, mean_phy)
pc = Correlation(phy_scores, chem_scores, n, sp, sc, mean_phy, mean_chem)
cm = Correlation(chem_scores, math_scores, n, sc, sm, mean_chem, mean_math)

print(round(mp, 2))
print(round(pc, 2))
print(round(cm, 2))
