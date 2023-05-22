from collections import defaultdict
from heapq import heappush, heappop
from math import inf
n, m = map(int, input().split())
AL = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    AL[a].append((b,c))
    AL[b].append((a,c))
    
distance = [inf for _ in range(n + 1)]
distance[1] = 0
frontier = [(0,1)]
while frontier:
    d, current = heappop(frontier)
    if d > distance[current]:
        continue
    for v, w in AL[current]:
        if d + w >= distance[v]:
            continue
        distance[v] = d + w
        heappush(frontier, (distance[v], v))
print(distance[n])
