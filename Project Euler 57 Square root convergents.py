# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input().strip())
numerators = [1]
denominators = [2]

for i in range(2, n + 1):
    numerators.append(denominators[-1])
    denominators.append(denominators[-1] * 2 + numerators[-2])

for i in range(n):
    numerator = denominators[i] + numerators[i]
    denominator = denominators[i]
    if len(str(numerator)) > len(str(denominator)):
        print(i + 1)
