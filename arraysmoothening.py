import heapq
from collections import Counter
N, K = map(int, input().split())
A = Counter(input().split())
pq = []
for k, v in A.items():
    heapq.heappush(pq, -v)
for _ in range(K):
    v = heapq.heappop(pq)
    heapq.heappush(pq, v+1)
print(heapq.heappop(pq) * -1)

