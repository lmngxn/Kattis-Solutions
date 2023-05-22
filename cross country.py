from heapq import heappush, heappop
from math import inf

N, S, T = map(int, input().split())
AM = [list(map(int, input().split())) for _ in range(N)]
dist = [inf] * N
dist[S] = 0
pq = [(0, S)]
while pq:
    d, current = heappop(pq)
    if d > dist[current]:
        continue
    for i in range(N):
        if i == current:
            continue
        if d + AM[current][i] >= dist[i]:
            continue
        dist[i] = d + AM[current][i]
        heappush(pq, (dist[i], i))
print(dist[T])
