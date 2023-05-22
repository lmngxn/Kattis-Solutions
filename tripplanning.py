from sys import stdin
N, M = map(int, stdin.readline().split())
train = [0] * N
counter = N
for i in range(M):
    a, b = map(int, stdin.readline().split())
    if abs(a - b) == N - 1:
        train[N-1] = i + 1
        counter -= 1

    elif abs(a - b) == 1:
        train[min(a, b) - 1] = i + 1
        counter -= 1

if counter:
    print('impossible')
else:
    print(*train, sep = '\n')

    
