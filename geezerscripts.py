from sys import stdin
from collections import defaultdict
from math import ceil
from heapq import heapify, heappush, heappop
#lost health set as positive to help maintain minheap
def lose_health(A, a, h):
    return (ceil(h/A) - 1) * a

A, H = map(int, stdin.readline().split())
n, m = map(int, stdin.readline().split())
AL = defaultdict(list)
for _ in range(m):
    start, end, a, h = map(int, stdin.readline().split())
    AL[start].append((end, lose_health(A, a, h)))
pq = []
max_health = [0] * (n + 1)
max_health[1] = H
for p, h_loss in AL[1]:
    if H <= h_loss:
        continue
    heappush(pq, (-(H - h_loss), p))
    max_health[p] = H - h_loss
while pq:
    current_H, current_p = heappop(pq)
    if current_p == n:
        print(-current_H)
        exit(0)
    for p, h_loss in AL[current_p]:
        if -current_H <= h_loss or -current_H - h_loss <= max_health[p]:
            continue
        heappush(pq, (current_H + h_loss, p))
        max_health[p] = -current_H - h_loss
print('Oh no')
