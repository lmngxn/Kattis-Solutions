from heapq import heappush, heappop
from collections import defaultdict
N, D = map(int, input().split())
C, *inf = map(int, input().split())
infected = set(inf)
enter = []
exit_room = []
for i in range(N):
    a, b = map(int, input().split())
    heappush(enter, (a, i+1))
    heappush(exit_room, (b, i+1))
AL = defaultdict(list)
room = set()
while exit_room:
    if (not enter) or exit_room[0][0] < enter[0][0]:
        t, p1 = heappop(exit_room)
        room.remove(p1)
    else:
        t, p1 = heappop(enter)
        for p2 in room:
            AL[p1].append(p2)
            AL[p2].append(p1)
        room.add(p1)
frontier = []
for p in infected:
    frontier.extend(AL[p])
counter = D
while counter > 0:
    next_frontier = []
    for p in frontier:
        if p not in infected:
            infected.add(p)
            next_frontier.extend(AL[p])
    frontier = next_frontier
    counter -= 1
print(*sorted(infected), sep = ' ')
