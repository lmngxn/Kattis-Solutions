N = 500001
from functools import reduce
parent = list(range(N))
size = [1] * N
rank = [0] * N
def find(i):
    children = []
    while parent[i] != i:
        children.append(i)
        i = parent[i]
    for c in children:
        parent[c] = i
    return i

def union(i, j):
    ip = find(i)
    jp = find(j)
    if ip == jp:
        return ip
    if rank[ip] < rank[jp]:
        parent[ip] = jp
        size[jp] += size[ip]
        return jp
    elif rank[jp] < rank[ip]:
        parent[jp] = ip
        size[ip] += size[jp]
        return ip
    else:
        parent[ip] = jp
        size[jp] += size[ip]
        rank[jp] += 1
        return jp

counter = 0
for _ in range(int(input())):
    num, *ingrd = map(int, input().split())
    total = 0
    components = set()
    for i in ingrd:
        if find(i) not in components:
            total += size[find(i)]
            components.add(find(i))
    if total == num:
        counter += 1
        if len(components) > 1:
            reduce(union, components)
print(counter)
