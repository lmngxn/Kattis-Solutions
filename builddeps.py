from sys import stdin
from collections import defaultdict, deque
n = int(stdin.readline())
rules = defaultdict(list)
dep = defaultdict(int)
no_dep = deque()
for _ in range(n):
    f, *lst = stdin.readline().split()
    if not lst:
        no_dep.append(f[:-1])
    else:
        for name in lst:
            rules[name.strip()].append(f[:-1])
            dep[f[:-1]] += 1
            
#topo sort kahn's algorithm
change = set([input()])
recompiled = []
while no_dep:
    current = no_dep.popleft()
    if current in change:
        recompiled.append(current)
        change.update(rules[current])
    for name in rules[current]:
        dep[name] -= 1
        if dep[name] == 0:
            no_dep.append(name)

print(*recompiled , sep = '\n')
