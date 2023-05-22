from collections import defaultdict, deque
N, M = map(int, input().split())
materials = list(map(int, input().split()))
AL = defaultdict(list)
root = set(range(N))
parent = [0] * N
for _ in range(M):
    u, v, w = map(int, input().split())
    AL[v].append((u, w))
    parent[u] += 1
    root.discard(u)
frontier = deque(root)
while frontier:
    current = frontier.popleft()
    for i, w in AL[current]:
        materials[i] += w * materials[current]
        parent[i] -= 1
        if parent[i] == 0 and i in AL:
            frontier.append(i)
print(*materials, sep = ' ')
