from heapq import heappush, heappop
def findset(i):
    if i == parents[i]:
        return i
    else:
        parents[i] = findset(parents[i])
        return parents[i]

def isSameSet(i, j):
    return findset(i) == findset(j)

def unionSet(i, j):
    if not isSameSet(i, j):
        x = parents[i]
        y = parents[j]
        if rank[x] == rank[y]:
            parents[y] = x
            rank[x] += 1
            size[x] += size[y]
        elif rank[x] > rank[y]:
            parents[y] = x
            size[x] += size[y]
        elif rank[y] > rank[x]:
            parents[x] = y
            size[y] += size[x]

N = int(input())
for _ in range(N):
    S, P = map(int, input().split())
    coordinates = []
    AM = [[0] * P for _ in range(P)]
    edge_list = []
    for i in range(P):
        x, y = map(int, input().split())
        coordinates.append((x,y))
        for j in range(len(coordinates) - 1):
            x1, y1 = coordinates[j]
            distance = ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5
            heappush(edge_list, (distance, i, j))

    parents = [i for i in range(P)]
    size = [1] * P
    rank = [1] * P
    connection = []
    while edge_list:
        d, a, b = heappop(edge_list)
        if not isSameSet(a, b):
            unionSet(a, b)
            connection.append((d, a, b))
        if size[findset(a)] == P:
            break

    connection.reverse()
    parents = [i for i in range(P)]
    size = [1] * P
    rank = [1] * P
    for i, edge in enumerate(connection):
        d, a, b = edge
        unionSet(a, b)
        if size[findset(a)] > S:
            print(f'{d:.2f}')
            break
        if size[findset(a)] == 0:
            print(f'{connection[i+1][0]:.2f}')
            break
