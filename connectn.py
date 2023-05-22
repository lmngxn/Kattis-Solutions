X, Y, N = map(int, input().split())
AM = [list(input().split()) for _ in range(X)]
def search(r, c, colour, n):
    direction = [(1,0), (0,1), (1,1), (1,-1)]
    for i, j in direction:
        for k in range(1, n):
            if c+j*k < 0 or r+i*k >= X or c+j*k >= Y or AM[r+i*k][c+j*k] != colour:
                break
            if k == n - 1:
                return True
    return False
for r in range(X):
    for c in range(Y - N + 1):
        if AM[r][c] == 'R' and search(r, c, 'R', N):
            print('RED WINS')
            exit(0)
        elif AM[r][c] == 'B' and search(r, c, 'B', N):
            print('BLUE WINS')
            exit(0)
print('NONE')
