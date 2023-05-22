m, n, s = map(int, input().split())
a_b = []
for _ in range(n):
    a_b.append(tuple(map(int, input().split())))
visited = set([s])
counter = 0
frontier = [s]
while frontier:
    counter += 1
    next_frontier = []
    for current in frontier:
        for a, b in a_b:
            temp = (current * a + b) % m
            if temp == 0:
                print(counter)
                exit(0)
            if temp not in visited:
                visited.add(temp)
                next_frontier.append(temp)
    frontier = next_frontier
print(-1)
