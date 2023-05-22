from collections import defaultdict
N = int(input())
items = [input() for _ in range(N)]
M = int(input())
suspicious = defaultdict(list)
for _ in range(M):
    a, b = input().split()
    suspicious[a].append(b)
    suspicious[b].append(a)
swap = [0, set(), set()]
tracker = 1
next_frontier = []
for item in items:
    if item in swap[1] or item in swap[-1]:
        continue
    swap[tracker].add(item)
    if item in suspicious:
        next_frontier = suspicious[item]
    while next_frontier:
        frontier, next_frontier = next_frontier, []
        tracker *= -1
        for i in frontier:
            if i in swap[-tracker]:
                print('impossible')
                exit(0)
            if i in swap[tracker]:
                continue
            swap[tracker].add(i)
            next_frontier.extend(suspicious[i])

print(*swap[1])
print(*swap[2])

            
