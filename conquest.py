from sys import stdin
from collections import defaultdict
from heapq import heappush, heappop
N, M = map(int, stdin.readline().split())
AL = defaultdict(list)
for _ in range(M):
    u, v = map(int, stdin.readline().split())
    AL[u].append(v)
    AL[v].append(u)
size = [int(stdin.readline()) for _ in range(N)]
spanning = size[0]
in_queue = set([1])
pq = []
for i in AL[1]:
    heappush(pq, (size[i-1], i))
    in_queue.add(i)
while pq and pq[0][0] < spanning:
    s, i = heappop(pq)
    spanning += s
    for j in AL[i]:
        if j not in in_queue:
            heappush(pq, (size[j-1], j))
            in_queue.add(j)
print(spanning)
