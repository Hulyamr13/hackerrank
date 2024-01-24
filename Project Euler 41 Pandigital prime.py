import itertools
def isprime(n):
    if n==1 or n%2==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

pandigitals=[]
for i in range(1,10):
    pandigitals+=[int(''.join(a)) for a in itertools.permutations([str(n) for n in range(1,i+1)]) if isprime(int(''.join(a)))]

for _ in range(int(input())):
    n=int(input())
    answer=-1
    for i in pandigitals[::-1]:
        if i<=n:
            answer=i
            break
    print(answer)