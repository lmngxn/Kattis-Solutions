from collections import defaultdict
N, M = map(int, input().split())
if N == 1:
    print('YES')
    exit(0)
visited = [0] * (N + 1)
AL = defaultdict(set)
for _ in range(M):
    a, b = map(int, input().split())
    AL[a].add(b)
    AL[b].add(a)
counter = 1
visited[1] = 1
frontier = list(AL[1])
while frontier:
    current = frontier.pop()
    if visited[current]:
        continue
    visited[current] = 1
    counter += 1
    if counter == N:
        print('YES')
        exit(0)
    frontier.extend(AL[current])
print('NO')
