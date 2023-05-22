from sys import stdin
from collections import defaultdict
n, m = map(int, stdin.readline().split())
money = list(int(stdin.readline()) for _ in range(n))
AL = defaultdict(list)
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    AL[a].append(b)
    AL[b].append(a)
visited = set()
for i in range(n):
    if i in visited:
        continue
    balance = money[i]
    visited.add(i)
    frontier = AL[i].copy()
    while frontier:
        current = frontier.pop()
        if current in visited:
            continue
        balance += money[current]
        visited.add(current)
        frontier.extend(AL[current])
    if balance != 0:
        print('IMPOSSIBLE')
        exit(0)
print('POSSIBLE')   
