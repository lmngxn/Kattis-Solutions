from collections import defaultdict
cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    visited = [0] * (n + 1)
    AL = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        AL[a].append(b)
        AL[b].append(a)
    visited[1] = 1
    frontier = [1]
    counter = 0
    while frontier:
        current = frontier.pop()
        for i in AL[current]:
            if visited[i] != 1:
                visited[i] = 1
                counter += 1
                frontier.append(i)
    print(counter)
            

"""
cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    AM = [[0]*n]*n
    for _ in range(m):
        a, b = map(int, input().split())
        AM[a-1][b-1] = 1
        AM[b-1][a-1] = 1
    visited = [0] * n
    visited[0] = 1
    frontier = [0]
    counter = 0
    while frontier:
        current = frontier.pop(0)
        for i in range(n):
            if not visited[i] and AM[current][i]:
                visited[i] = 1
                frontier.append(i)
                counter += 1
    print(counter)
"""
