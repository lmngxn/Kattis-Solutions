def check(r, c, move, board):
    check = [(r-1,c-2),(r-2,c-1),(r+1,c-2),(r-2,c+1),\
             (r-1,c+2),(r+2,c-1),(r+1,c+2),(r+2,c+1)]
    result = []
    for r, c in check:
        if 0 <= r < N and 0 <= c < N:
            if board[r][c] == '.':
                result.append((r,c))
                board[r][c] = move + 1
    return result   

N = int(input())
board = []
for i in range(N):
    line = input()
    if 'K' in line:
        r, c = i, line.index('K')
    board.append([i for i in line])

board[r][c] = 0
frontier = [(r, c)]
while frontier:
    r, c = frontier.pop(0)
    move = board[r][c]
    if (r,c) == (0,0):
        break
    frontier.extend(check(r, c, move, board))

if board[0][0] == '.':
    print(-1)
else:  
    print(move)

