n = int(input())
while n != -1:
    triangle = set()
    weak = set()
    AM = [list(map(int, input().split())) for _ in range(n)]
    for v in range(n):
        if sum(AM[v]) < 2:
            weak.add(v)
        else:
            for i in range(v+1, n - 1):
                if AM[v][i] == 0 or i in weak:
                    continue
                for j in range(i+1, n):
                    if AM[v][j] == 0 or j in weak:
                        continue
                    if AM[i][j] == 1:
                        triangle.update([v,i,j])
            if v not in triangle:
                weak.add(v)
    print(*sorted(weak))
    n = int(input())
