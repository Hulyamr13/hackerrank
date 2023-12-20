def size(node):
    if node:
        return node.size
    return 0


class Node:

    def __init__(self, id=-1):
        self.id = id
        self.left = None
        self.right = None
        self.parent = None
        self.size = 1
        self.rev = False

    def release(self):
        if self.rev:
            self.rev = False
            self.left, self.right = self.right, self.left
            if self.left:
                self.left.rev ^= True
            if self.right:
                self.right.rev ^= True

    def update(self):
        self.size = 1 + size(self.left) + size(self.right)


def zig(p):
    q = p.parent
    r = q.parent
    q.left = p.right
    if q.left:
        q.left.parent = q
    p.right = q
    q.parent = p
    p.parent = r

    if p.parent:
        if r.left == q:
            r.left = p
        if r.right == q:
            r.right = p
    q.update()


def zag(p):
    q = p.parent
    r = q.parent
    q.right = p.left
    if q.right:
        q.right.parent = q
    p.left = q
    q.parent = p
    p.parent = r
    if p.parent:
        if r.left == q:
            r.left = p
        if r.right == q:
            r.right = p
    q.update()


def splay(root, p, b=None):
    p.release()
    while p.parent != b:
        q = p.parent

        if q.parent == b:
            q.release()
            p.release()
            if q.left == p:
                zig(p)
            else:
                zag(p)
        else:
            r = q.parent
            r.release()
            q.release()
            p.release()
            if r.left == q:
                if q.left == p:
                    zig(q)
                    zig(p)
                else:
                    zag(p)
                    zig(p)
            elif q.left == p:
                zig(p)
                zag(p)
            else:
                zag(q)
                zag(p)
    p.update()
    if b == None:
        root = p
    else:
        b.update()
    return root


def find(k, p):
    if not p or p.size < k:
        return None
    while k:
        p.release()
        if p.left and p.left.size >= k:
            p = p.left
        else:
            if p.left:
                k -= p.left.size
            k -= 1
            if k > 0:
                p = p.right
    return p


def build(a, b):
    global T

    if a > b:
        return None
    if a == b:
        prx = T[a]
        prx.left = None
        prx.right = None
        prx.parent = None

        return prx
    mid = (a + b) // 2
    prx = T[mid]
    prx.parent = None

    prx.left = build(a, mid - 1)

    if prx.left:
        prx.left.parent = prx
    prx.right = build(mid + 1, b)
    if prx.right:
        prx.right.parent = prx
    prx.update()

    return prx


def reverse(root, a, b):
    if a == b:
        return
    lfx = a + 1
    rgx = b + 1
    prev = find(lfx - 1, root)
    nxt = find(rgx + 1, root)
    root = splay(root, prev)
    root = splay(root, nxt, prev)
    nxt.left.rev ^= True
    return root


n, q = map(int, input().split())

T = [None for i in range(n + 2)]
for i in range(n + 2):
    T[i] = Node(i)

root = build(0, n + 1)

s = ''
for k in range(q):

    query = tuple(map(int, input().split()))
    t = query[0]

    if t == 1:
        i, j = query[1], query[2]
        root = reverse(root, i, j)

    elif t == 2:
        i = query[1]
        ptx = T[i]
        root = splay(root, ptx)
        s += 'element {} is at position {}\n'.format(i, size(ptx.left))

    else:
        i = query[1]
        ptx = find(i + 1, root)
        s += 'element at position {} is {}\n'.format(i, ptx.id)
print(s)