from math import gcd

def solutionExists(L, x, dx):
    if dx == 0:
        return x == 0
    return x % gcd(L, dx) == 0

diafant_cache = {}

def diafantSolution(a, b, c):
    key = f"{a},{b},{c}"
    if key in diafant_cache:
        return diafant_cache[key]
    a1, b1 = 1, 0
    a2, b2 = 0, 1
    while b:
        d = (a - a % b) // b
        a, b = b, a - d * b
        a1, b1 = b1, a1 - d * b1
        a2, b2 = b2, a2 - d * b2
    x0, y0 = a1 * c // a, a2 * c // a
    x1, y1 = b1, b2
    if x1 < 0:
        x1, y1 = -x1, -y1
    while x0 < 0:
        x0 += x1
        y0 += y1
    while x0 - x1 > 0:
        x0 -= x1
        y0 -= y1
    diafant_cache[key] = (x0, y0, x1, y1)
    return x0, y0, x1, y1

def step(L, x, dx):
    start = 0
    while start <= L and start * dx % L != x:
        start += 1
    if start == L + 1:
        return None
    step = 1
    while (start + step) * dx % L != x:
        step += 1
    return start, step

def dxAndSteps(L, xs, xm, N):
    result = {}
    for dx in range(-N, N + 1):
        if dx % L in result:
            continue
        r = []
        if solutionExists(L, xs, dx):
            r.append(step(L, xs, dx))
        if xs != xm:
            if solutionExists(L, xm, dx):
                r.append(step(L, xm, dx))
        if r:
            result[dx % L] = r
    return result

def hit(nxs, nys, nzs):
    for nx in nxs:
        startX, stepX = nx
        for ny in nys:
            startY, stepY = ny
            if stepX == stepY and startX != startY:
                continue
            for nz in nzs:
                startZ, stepZ = nz
                if stepX == stepZ and startX != startZ:
                    continue
                if stepZ == stepY and startZ != startY:
                    continue
                m14 = stepX * (startZ - startY)
                m24 = stepY * (startZ - startX)
                m34 = stepZ * (startY - startX)
                gcd123 = gcd(stepX * gcd(stepY, stepZ), stepY * stepZ)
                if m14 % gcd123 == m24 % gcd123 == m34 % gcd123 == 0:
                    return True
    return False

def shortestPath(nxs, nys, nzs, limit):
    result = limit
    for nx in nxs:
        startX, stepX = nx
        for ny in nys:
            startY, stepY = ny
            if stepX == stepY and startX != startY:
                continue
            for nz in nzs:
                startZ, stepZ = nz
                if stepX == stepZ and startX != startZ:
                    continue
                if stepZ == stepY and startZ != startY:
                    continue
                x0, _, x1, _ = diafantSolution(stepX, -stepY, startY - startX)
                m14 = stepX * (startZ - startY)
                m24 = stepY * (startZ - startX)
                m34 = stepZ * (startY - startX)
                gcd123 = gcd(stepX * gcd(stepY, stepZ), stepY * stepZ)
                if m14 % gcd123 == m24 % gcd123 == m34 % gcd123 == 0:
                    z0, _, _, _ = diafantSolution(-stepZ, stepX * x1, startZ - startX - stepX * x0)
                    newRes = startZ + stepZ * z0
                    result = min(result, newRes)
    return result

def solve(L, W, H, x1, y1, z1, x2, y2, z2, x0, y0, z0, N):
    L += L
    W += W
    H += H
    x1s, x1m = (x1 - x0) % L, (L - x1 - x0) % L
    x2s, x2m = (x2 - x0) % L, (L - x2 - x0) % L
    y1s, y1m = (y1 - y0) % W, (W - y1 - y0) % W
    y2s, y2m = (y2 - y0) % W, (W - y2 - y0) % W
    z1s, z1m = (z1 - z0) % H, (H - z1 - z0) % H
    z2s, z2m = (z2 - z0) % H, (H - z2 - z0) % H
    DX1 = dxAndSteps(L, x1s, x1m, N)
    DY1 = dxAndSteps(W, y1s, y1m, N)
    DZ1 = dxAndSteps(H, z1s, z1m, N)
    DX2 = dxAndSteps(L, x2s, x2m, N)
    DY2 = dxAndSteps(W, y2s, y2m, N)
    DZ2 = dxAndSteps(H, z2s, z2m, N)
    result1 = 0
    result2 = 0
    limit = L * W * H
    cache = {}
    for dxx in range(-N, N + 1):
        for dyy in range(-N, N + 1):
            gxy = gcd(dxx, dyy)
            for dzz in range(-N, N + 1):
                if dxx == dyy == dzz == 0:
                    continue
                g = gcd(gxy, dzz)
                dx, dy, dz = (dxx // g) % L, (dyy // g) % W, (dzz // g) % H
                key = (dx * limit + dy) * limit + dz
                if key in cache:
                    r1, r2 = cache[key]
                    result1 += r1
                    result2 += r2
                    continue
                firstHit, secondHit = False, False
                if dx in DX1 and dy in DY1 and dz in DZ1:
                    firstHit = hit(DX1[dx], DY1[dy], DZ1[dz])
                if dx in DX2 and dy in DY2 and dz in DZ2:
                    secondHit = hit(DX2[dx], DY2[dy], DZ2[dz])
                if firstHit and secondHit:
                    N1 = shortestPath(DX1[dx], DY1[dy], DZ1[dz], limit = limit)
                    N2 = shortestPath(DX2[dx], DY2[dy], DZ2[dz], limit = N1 + 1)
                    if N1 < N2:
                        result1 += 1
                        cache[key] = (1, 0)
                    else:
                        result2 += 1
                        cache[key] = (0, 1)
                elif firstHit:
                    result1 += 1
                    cache[key] = (1, 0)
                elif secondHit:
                    result2 += 1
                    cache[key] = (0, 1)
    return result1, result2

if __name__ == "__main__":
    input()
    L, W, H, x1, y1, z1, x2, y2, z2, x0, y0, z0, N = list(map(int, input().split()))
    r1, r2 = solve(L = L, W = W, H = H, x1 = x1, y1 = y1, z1 = z1, x2 = x2, y2 = y2, z2 = z2, x0 = x0, y0 = y0, z0 = z0, N = N)
    print(f"{r1} {r2}")
