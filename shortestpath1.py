from heapq import heapify, heappush, heappop
from collections import defaultdict
INF = int(1e9)
n, m, q, s = map(int, input().split())
while sum([n, m, q, s]):
    AL = [[] for _ in range(n)]
    incoming = [0] * n
    root = {i for i in range(n)}
    for _ in range(m):
        u, v, w = map(int, input().split())
        AL[u].append((v,w))
        incoming[v] += 1
        root.discard(v)

    # topological sort
    sort = list(root)
    frontier = heapify(list((0, r) for r in root))
    
    while frontier:
        dist, current = heappop(frontier)
        for v, w in AL[current]:
            incoming[v] -= 1
            if not incoming[v]:
                sort.append(v)
                heappush(frontier, (dist + w, v))

    # (Modified) Dijkstra's routine
    dist = [INF for u in range(n)]
    dist[s] = 0
    pq = []
    heappush(pq, (0, s))

    # sort the pairs by non-decreasing distance from s
    while pq:                    # main loop
        d, u = heappop(pq)                  # shortest unvisited u
        if (d > dist[u]): continue          # a very important check
        for v, w in AL[u]:                  # all edges from u
            if (dist[u]+w >= dist[v]): continue # not improving, skip
            dist[v] = dist[u]+w             # relax operation
            heappush(pq, (dist[v], v))  

    for _ in range(q):
        u = int(input())
        if dist[u] == INF:
            print('Impossible')
        else:
            print(dist[u])
    print()
    n, m, q, s = map(int, input().split())
