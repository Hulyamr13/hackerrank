import collections
lim = 10**6+1
dist = [0]*lim
active = collections.deque()
active.append(0)
while active:
   n = active.popleft()
   d = dist[n]+1
   x = n + 1
   if x < lim and dist[x] == 0:
      dist[x] = d
      active.append(x)
   for m in range(2,n+1):
      x = m * n
      if x >= lim: break
      if dist[x] == 0:
         dist[x] = d
         active.append(x)
Q = int(input())
for q in range(Q):
   N = int(input())
   print(dist[N])