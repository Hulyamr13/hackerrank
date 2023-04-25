def calculate(A,B,C,k):
    n = max(len(A), len(B), len(C))
    A,B,C = ([0]*(n-len(x)) + x for x in (A,B,C))
    for i,a,b,c in zip(range(n),A,B,C):
        #print(*(A,B,C), sep="\n")
        if a | b < c:
            B[i] = 1
            k -= 1
        elif a | b > c:
            k -= a + b
            A[i] = B[i] = 0
        if k < 0:
            return [-1]
        #print(k)
    for i,a,b in zip(range(n), A,B):
        if a > b and k >= 2:
            A[i],B[i] = 0, 1
            k -= 2
        elif a >= b >= 1 and k:
            A[i] = 0
            k -= 1
    A,B = (hex(int("".join(map(str, x)), 2))[2:].upper() for x in (A,B))
    return A,B

def main():
    q = int(input())
    for i in range(q):
        k = int(input())
        a,b,c = (list(map(int, bin(int(input(), 16))[2:])) for i in range(3))
        print(*calculate(a,b,c,k), sep="\n")

if __name__ == '__main__':
    main()
