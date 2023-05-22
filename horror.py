from sys import stdin
from collections import defaultdict, deque
N, H, L = map(int, stdin.readline().split())
horror = set(map(int, stdin.readline().split()))
distance = [1000] * N
for m in horror:
    distance[m] = 0
AL = defaultdict(list)
for _ in range(L):
    a, b = map(int, stdin.readline().split())
    AL[a].append(b)
    AL[b].append(a)
frontier = deque(horror)
while frontier:
    current = frontier.popleft()
    for m in AL[current]:
        if distance[current] + 1 < distance[m]:
            distance[m] = distance[current] + 1
            frontier.append(m)
print(distance.index(max(distance)))
