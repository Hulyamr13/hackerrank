# Enter your code here. Read input from STDIN. Print output to STDOUT

def sum_of_hackerrank_numbers(A, B):
    def gcd(x, y):
        while y != 0:
            (x, y) = (y, x % y)
        return x

    def sumProdOneDivider(divider, limit):
        count = limit // divider
        return divider * (count + 1) * count // 2, count

    def get(result, x, limit):
        items = list(result.items())[:]
        if x not in result:
            result[x] = 0
        result[x] += 1
        if result[x] == 0:
            del result[x]
        for d, v in items:
            dx = d * x
            if dx > limit:
                continue
            if dx not in result:
                result[dx] = 0
            result[dx] -= v
            if result[dx] == 0:
                del result[dx]
        return result

    def getInterval(start, finish, limit):
        result = {}
        for x in range(start, finish):
            items = list(result.items())[:]
            isdiv = False
            for d in range(start, x):
                if x % d == 0:
                    isdiv = True
                    break
            if isdiv:
                continue
            result[x] = 1
            for d, v in items:
                dx = d * x // gcd(d, x)
                if dx > limit:
                    continue
                if dx not in result:
                    result[dx] = 0
                result[dx] -= v
                if result[dx] == 0:
                    del result[dx]
        return result

    def sumProd(A, B):
        all = set()
        s = 0
        l = 0
        for x in range(A, 0, -1):
            process = getInterval(x, A + 1, A * B)
            for d, v in process.items():
                sx0, lx0 = sumProdOneDivider(d, B * (x - 1))
                sx1, lx1 = sumProdOneDivider(d, B * x)
                s += v * (sx1 - sx0)
                l += v * (lx1 - lx0)
        return s, l

    def sumXor(A, B):
        if B < 100:
            def sumXorRef(A, B):
                all = set()
                for x in range(1, A + 1):
                    for y in range(1, B + 1):
                        all.add(x ^ y)
                return sum(all), len(all)

            return sumXorRef(A, B)
        b = B - 100
        s = b * (b + 1) // 2
        l = b + 1
        all = set()
        for x in range(1, A + 1):
            for y in range(b + 1, B + 1):
                xy = x ^ y
                if xy <= b:
                    continue
                all.add(xy)
        s += sum(all)
        l += len(all)
        return s, l

    prod, nprod = sumProd(A, B)
    xor, nxor = sumXor(A, B)
    result = prod * nxor * pow(10, len("%d" % B) + 1) + nprod * xor
    return result

A, B = map(int, input().split())
result = sum_of_hackerrank_numbers(A, B)
print(result)
