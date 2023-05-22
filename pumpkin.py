P, D, N = map(int, input().split())
pumpkin = []
for _ in range(P):
    R, C = map(int, input().split())
    pumpkin.append((R, C))
grid = [[-1] * N for _ in range(N)]
root = []
for i, RC in enumerate(pumpkin):
    R, C = RC
    grid[R][C] = (0, i)
    root.append([(R,C), (R,C), (R,C), (R,C)])
dead = set()
dead_time = [-1] * P
def expand(i, counter):
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    new_root = []
    for j in range(4):
        R, C = root[i][j]
        R += move[j][0]
        if R < 0 or R >= N:
            dead.add(i)
            dead_time[i] = counter
            continue
        C += move[j][1]
        if C < 0 or C >= N:
            dead.add(i)
            dead_time[i] = counter
            continue
        if grid[R][C] == -1:
            grid[R][C] = (counter, i)
        else:
            dead.add(i)
            dead_time[i] = counter
            if grid[R][C][0] == counter:
                dead.add(grid[R][C][1])
                dead_time[grid[R][C][1]] = counter
        new_root.append((R, C))
    root[i] = new_root
for i in range(1, D+1):
    for j in range(P):
        if j in dead:
            continue
        expand(j, i)
    if len(dead) == P:
        break
for t in dead_time:
    print('ALIVE' if t == -1 else t)
