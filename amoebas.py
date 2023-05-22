m, n = map(int, input().split())
grid = [[*input()] for _ in range(m)]
def loop(r, c):
    tag = grid[r][c]
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == j == 0:
                continue
            if r + i < 0 or r + i >= m:
                continue
            if c + j < 0 or c + j >= n:
                continue
            if grid[r+i][c+j] == '#':
                grid[r+i][c+j] = tag
                loop(r+i, c+j)

counter = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == '#':
            counter += 1
            grid[i][j] = counter
            loop(i, j)
print(counter)
