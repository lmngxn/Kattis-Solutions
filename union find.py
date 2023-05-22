N, Q = map(int, input().split())
sets = list(range(N))
rank = [0] * (N)
def find(i):
    temp = i
    children = []
    while sets[i] != i:
        children.append(i)
        i = sets[i]
    for c in children:
        sets[c] = i
    return i

def union(i, j):
    ip = find(i)
    jp = find(j)
    if ip == jp:
        return
    if rank[ip] < rank[jp]:
        sets[ip] = jp
    elif rank[jp] < rank[ip]:
        sets[jp] = ip
    else:
        sets[ip] = jp
        rank[jp] += 1

for _ in range(Q):
    op, i, j = input().split()
    if op == '=':
        union(int(i), int(j))
    else:
        if find(int(i)) == find(int(j)):
            print('yes')
        else:
            print('no')
