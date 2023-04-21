import heapq

def find(V,N,S):
    dist=[-1 for x in range(N)]
    visited=[False for x in range(N)]
    Q=[(0,S)] #use a priority queue
    dist[S]=0
    while Q:
        mindist,minv=heapq.heappop(Q)
        if not visited[minv]:
            for x in V[minv]:
                if dist[x] == -1: dist[x]=mindist+V[minv][x]
                else: dist[x]=min(dist[x],mindist+V[minv][x])
                heapq.heappush(Q,(dist[x],x))
            visited[minv]=True
    del dist[S]
    for x in dist: print(x,end=' ')
    print()

def update(V,X,Y,R):
    if Y not in V[X]: V[X][Y]=R
    else: V[X][Y]=min(V[X][Y],R)

def main():
    T=int(input())
    for _ in range(T):
        N,M=(int(x) for x in input().split())
        V=[dict() for x in range(N)]
        for i in range(M):
            X,Y,R=(int(x) for x in input().split())
            X,Y=X-1,Y-1
            update(V,X,Y,R)
            update(V,Y,X,R)
        find(V,N,int(input())-1)

if __name__ == "__main__":
    main()