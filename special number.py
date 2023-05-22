from heapq import heappush, heappop
pq = [(1,0,0,0)]
track = set()
n = 50
for _ in range(50):
    num, i, j, k = heappop(pq)
    print(num, i, j, k)
    for a, b, c in [(1,0,0), (0,1,0), (0,0,1)]:
        if (i+a, j+b, k+c) not in track:
            heappush(pq, (2 ** (i+a) * 3 ** (j+b) * 5 ** (k+c), i+a, j+b, k+c))
            track.add((i+a, j+b, k+c))

    
