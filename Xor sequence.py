from math import ceil, floor

def xorSequence(l, r):
    val = 0

    if r - l + 1 > 4:
        if l % 4 == 0:
            val ^= l ^ 1 ^ (l + 3)
            l += 3

        elif l % 4 == 1:
            val ^= 1 ^ (l + 2)
            l += 2

        elif l % 4 == 2:
            val ^= l + 1
            l += 1

        if r % 4 == 0:
            val ^= r
            r -= 1

        elif r % 4 == 1:
            val ^= 1 ^ (r - 1)
            r -= 2

        elif r % 4 == 2:
            val ^= (r + 1) ^ 1 ^ (r - 2)
            r -= 3

        if ((r - l) / 4) % 2 == 1:
            val ^= 2

    else:
        for i in range(l, r + 1):
            if i % 4 == 1:
                val ^= 1
            elif i % 4 == 2:
                val ^= i + 1
            elif i % 4 == 0:
                val ^= i

    return val


if __name__ == '__main__':
    q = int(input().strip())  # Number of questions

    for q_itr in range(q):
        lr = input().strip().split(' ')
        l = int(lr[0])
        r = int(lr[1])
        result = xorSequence(l, r)
        print(result)