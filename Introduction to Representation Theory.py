# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

n, k = map(int, input().split())

real = []
imag = []
PI = 3.14159265358979

for _ in range(k):
    a, b = map(float, input().split())
    real.append(a)
    imag.append(b)

for i in range(k):
    sum_real = 0

    for j in range(k):
        modded = (i * j) % k
        sum_real += real[j] * math.cos(2 * modded * PI / k) - imag[j] * math.sin(2 * modded * PI / k)

    sum_real = sum_real / k + 0.5
    how_many = int(sum_real)

    x = math.cos(2 * i * PI / k)
    y = -math.sin(2 * i * PI / k)

    for _ in range(how_many):
        print(f"{x:.7f} {y:.7f}")
