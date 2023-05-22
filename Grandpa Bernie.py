from collections import defaultdict
n = int(input())
memo = defaultdict(list)
sort = dict()
for _ in range(n):
    s, y = input().split()
    memo[s].append(int(y))
q = int(input())
for _ in range(q):
    s, k = input().split()
    if not sort.get(s, 0):
        sort[s] = 1
        memo[s].sort()
    print(memo[s][int(k) - 1])
