from heapq import heappush, heappop
from math import inf
n = int(input())
spots = []
for _ in range(n + 2):
    x, y = map(int, input().split())
    spots.append((x, y))
dist = [inf] * (n + 2)
dist[n] = 0
dist[n+1] = (spots[n][0] - spots[n+1][0]) ** 2 + (spots[n][1] - spots[n+1][1]) ** 2
parent = [-1] * (n + 2)
pq = [(0, n)]
AM = [[0] * (n+2) for _ in range(n+2)]

while pq:
    d, i = heappop(pq)
    if d > dist[i]:
        continue
    if i == n+1:
        break
    x1, y1 = spots[i]
    for j in range(n + 2):
        x2, y2 = spots[j]
        if AM[i][j] == 0:
            AM[j][i] = AM[i][j] = (x1 - x2) ** 2 + (y1 - y2) ** 2
        if d + AM[i][j] >= dist[j]:
            continue
        dist[j] = d + AM[i][j]
        parent[j] = i
        heappush(pq, (dist[j], j))

route = []
prev = parent[n+1]
while prev != -1:
    route.append(prev)
    prev = parent[prev]
if route:
    route.reverse()
    print(*route, sep = '\n')
else:
    print('-')
