from sys import stdin

N, M = map(int, stdin.readline().split())
while N + M != 0:
    memo = set(stdin.readline() for _ in range(N))
    counter = 0
    for _ in range(M):
        if stdin.readline() in memo:
            counter += 1
    print(counter)
    N, M = map(int, stdin.readline().split())
