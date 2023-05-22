N = int(input())
AM = [list(map(int, input().split())) for  _ in range(N)]
counter = 0
for i in range(N - 2):
    for j in range(i+1, N - 1):
        if AM[i][j]:
            for k in range(j+1, N):
                if AM[i][k] and AM[j][k]:
                    counter += 1
print(counter)
