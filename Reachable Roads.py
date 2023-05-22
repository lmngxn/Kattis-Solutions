from collections import defaultdict
n = int(input())
for _ in range(n):
    m = int(input())
    r = int(input())
    memo = defaultdict(list)
    for _ in range(r):
        a, b = map(int, input().split())
        memo[a].append(b)
        memo[b].append(a)
    visited = set()
    count = -1
    for i in range(m):
        if i in visited:
            continue
        frontier = [i]
        count += 1
        while frontier:
            curr = frontier.pop(-1)
            if curr not in visited:
                visited.add(curr)
                frontier.extend(memo[curr])
    print(count)  
