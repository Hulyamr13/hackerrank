# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools
import math

n = 5 * 10**6
answers = [0] * (n + 1)

for item in itertools.combinations(range(1, int(n**0.5) + 1, 2), r=2):
    t = item[0]
    s = item[1]
    if math.gcd(s, t) == 1:
        for i in range(s * (s + t), n + 1, s * (s + t)):
            answers[i] += 1

max_tri = 0
answer = 0
final_answers = []

for i in range(0, n + 1):
    value = answers[i]
    if value > max_tri:
        answer = i
        max_tri = value
    final_answers.append(answer)

for _ in range(int(input())):
    n = int(input())
    print(final_answers[n])
