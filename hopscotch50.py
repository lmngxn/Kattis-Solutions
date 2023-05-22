from collections import defaultdict
from math import inf
from heapq import heappop, heappush
n, k = map(int, input().split())
pos = defaultdict(list)
for i in range(n):
    for j, x in enumerate(map(int, input().split())):
        pos[x].append((i, j))

for i in range(1, k+1):
    if not pos[i]:
        print(-1)
        exit(0)

shortest = [[inf] * n  for _ in range(n)]
min_d = inf
for r, c in pos[1]:
    shortest[r][c] = 0 
    pq = [(0, 1, r, c)]
    while pq:
        d, current, r1, c1 = heappop(pq)
        if d > shortest[r1][c1]:
            continue
        for r2, c2 in pos[current + 1]:
            w = abs(r2 - r1) + abs(c2 - c1)
            if d + w >= shortest[r2][c2]:
                continue
            shortest[r2][c2] = d + w
            if current + 1 < k:
                heappush(pq, (shortest[r2][c2], current + 1, r2, c2))
            if current + 1 == k and shortest[r2][c2] < min_d:
                min_d = shortest[r2][c2]
print(min_d)
