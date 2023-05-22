from collections import defaultdict, deque
from heapq import heappush, heappop
from math import inf
n, m = map(int, input().split())
languages = dict()
for language in input().split():
    languages[language] = 0
AL = defaultdict(list)
for _ in range(m):
    l1, l2, c = input().split()
    if l2 != 'English':
        AL[l1].append((l2, int(c)))
    if l1 != 'English':
        AL[l2].append((l1, int(c)))

cost = dict()
cost['English'] = 0
frontier = ['English']
counter = 0
depth = 1
while frontier:
    next_frontier = set()
    for current in frontier:
        for l, c in AL[current]:
            if languages[l] == 0:
                languages[l] = depth
                next_frontier.add(l)
                cost[l] = c
                counter += 1
            elif languages[l] == depth:
                if cost[l] > c:
                    cost[l] = c
    if counter == n:
        break
    frontier = next_frontier
    depth += 1
print(sum(cost.values()) if counter == n else 'Impossible')
