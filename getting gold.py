W, H = map(int, input().split())
maze =[[x for x in input()] for i in range(H)]

print(maze)

for i in range(H):
    if 'P' in maze[i]:
        r, c = i, maze[i].index('P')

gold = [0]

def has_draft(r, c):
    return maze[r+1][c] == 'T' or maze[r-1][c] == 'T' or maze[r][c+1] == 'T' or maze[r][c-1] == 'T'

def search(r, c):
    if maze[r][c] == '#':
        return 
    if maze[r][c] == 'G':
        gold[0] += 1
    #sink the route moved
    maze[r][c] = '#'
    if has_draft(r, c):
        return 
    search(r+1, c)
    search(r-1, c)
    search(r, c+1)
    search(r, c-1)
    return 

search(r, c)

print(gold[0])
