N, M = map(int, input().split())
grid = [[*input()] for _ in range(N)]
def propagate(r, c):
    if grid[r+1][c] == '.':
        grid[r+1][c] = 'V'
    elif grid[r+1][c] == '#':
        if c-1 >= 0 and grid[r][c-1] == '.':
            grid[r][c-1] = 'V'
            propagate(r, c-1)
        if c+1 < M and grid[r][c+1] == '.':
            grid[r][c+1] = 'V'
            propagate(r, c+1)
r = 0
while r < N - 1:
    for c in range(M):
        if grid[r][c] == 'V':
           propagate(r, c)                    
    r += 1
for row in grid:
    print(*row, sep = '')
