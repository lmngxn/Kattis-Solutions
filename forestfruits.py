from collections import defaultdict
from heapq import heapify, heappush, heappop
V, E, C, K, M = map(int, input().split())
if C < M and C < K:
    print(-1)
    exit(0)
AL = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    AL[u].append((w,v))
    AL[v].append((w,u))
clearings = set(map(int, input().split()))
counter = 0
clearing_dist = []
frontier = [(0,1)]
visited = set()
while counter < C and frontier:
    distance, c = heappop(frontier)
    if c in visited:
        continue
    visited.add(c)
    if c in clearings:
        clearing_dist.append(distance * 2)
        counter += 1
    for d, v in AL[c]:
        heappush(frontier, (distance + d, v))
if counter < M and counter < K:
    print(-1)
    exit(0)
if M < counter:
    print(sorted(clearing_dist)[M - 1])
elif K < counter:
    print(max(sorted(clearing_dist)[:K]))
else:
    print(max(clearing_dist))
