def search(r, c, grid, visited):
    move = [(r+1,c, 'U'), (r-1, c, 'D'), (r,c+1,'L'), (r,c-1,'R')]
    result = []
    for i, j, d in move:
        if (i,j) in visited:
            continue
        if grid[i][j] == '0' or grid[i][j] == d:
            result.append((i, j))
    return result

time, N, M = map(int, input().split())
grid = []
start = ''
for i in range(N):
    row = input()
    if not start:
        for j in range(M):
            if row[j] == 'S':
                start = (i, j)
                break
    grid.append([*row])
visited = set()
frontier = [start]
for t in range(time + 1):
    next_frontier = set()
    for r, c in frontier:
        if r == 0 or r == N-1 or c == 0 or c == M-1:
            print(t)
            exit(0)
        visited.add((r,c))
        next_frontier.update(search(r, c, grid, visited))
    frontier = next_frontier
print('NOT POSSIBLE')
