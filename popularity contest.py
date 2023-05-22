N, M = map(int ,input().split())
friends = [-i for i in range(N+1)]
for _ in range(M):
    a, b = map(int ,input().split())
    friends[a] += 1
    friends[b] += 1
print(*friends[1:], sep=' ')
