from collections import defaultdict, deque
C, P, X, L = map(int, input().split())
if X == L:
    [input() for _ in range(P)]
    print('leave')
    exit(0)
trading_partners = [0] * (C + 1)
AL = defaultdict(set)
for _ in range(P):
    a, b = map(int, input().split())
    trading_partners[a] += 0.5
    trading_partners[b] += 0.5
    AL[a].add(b)
    AL[b].add(a)
left = set()

frontier = set([L])
while frontier:
    current = frontier.popleft()
    left.add(current)
    for country in AL[current]:
        if country in left:
            continue
        trading_partners[country] -= 1
        if trading_partners[country] <= 0:
            if country == X:
                print('leave')
                exit(0)
            frontier.add(country)
print('stay')
