def mex(l):
    l = sorted(set(l))
    for i,x in enumerate(l):
        if i != x:
            return i
    return len(l)

def sg(n, sg_cache=None):
    if n <= 2:
        return 0
    if sg_cache and not (sg_cache[n] is None):
        return sg_cache[n]
    def successors(m, beg):
        l = []
        for i in range(beg+1,(1+m)//2):
            sgi = sg(i, sg_cache)
            l.append(sgi ^ sg(m-i, sg_cache))
            for j in successors(m-i, i):
                l.append(sgi ^ j)
        return l
    ret = mex(successors(n, 0))
    sg_cache[n] = ret
    return ret

def sgl(l):
    sg_cache = [0,0,0]+[None]*(max(l)-2)
    ret = 0
    for n in l:
        ret ^= sg(n, sg_cache)
    return ret, sg_cache

def stonePiles(arr):
    return ["BOB","ALICE"][sgl(arr)[0] != 0]


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        result = stonePiles(arr)
        print(result)
