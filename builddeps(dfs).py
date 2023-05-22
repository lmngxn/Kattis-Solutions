from sys import stdin, setrecursionlimit
from collections import defaultdict, deque
setrecursionlimit(1000000)
#dfs function with topo
def dfs(x):
    for name in rules[x]:
        if name in visited:
            continue
        dfs(name)
    visited.add(x)
    topo.append(x)

n = int(stdin.readline())
rules = defaultdict(list)
no_dep = []
visited = set()
for _ in range(n):
    f, *lst = stdin.readline().split()
    if not lst:
        no_dep.append(f[:-1])
    else:
        for name in lst:
            rules[name.strip()].append(f[:-1])

#topo sort
topo = []
for x in no_dep:
    dfs(x)
topo.reverse()

#remove not affected elements 
change = set([input()])
recompiled = []
for name in topo:
    if name not in change:
        continue
    recompiled.append(name)
    change.update(rules[name])

print(*recompiled , sep = '\n')
