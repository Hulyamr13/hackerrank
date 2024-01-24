# Enter your code here. Read input from STDIN. Print output to STDOUT

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    if all(n % i for i in range(3, int(n**0.5) + 1, 2)):
        return True
    return False

n = int(input().strip())
s = 0

for i in range(10, n + 1):
    if is_prime(i):
        t = i
        while t > 0:
            if not is_prime(t):
                break
            t = t % (10**(len(str(t)) - 1))

        if t == 0:
            t = i
            while t > 0:
                if not is_prime(t):
                    break
                t = t // 10

            if t == 0:
                s += i

print(s)
