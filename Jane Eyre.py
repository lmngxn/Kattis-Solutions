import heapq
n, m, k = map(int, input().split())
pq = [('Jane Eyre', k)]
heapq.heapify(pq)
for _ in range(n):
    _, a, b = input().split("\"")
    if a < 'Jane Eyre':
        heapq.heappush(pq,(a, int(b)))
print(pq)
friend = []
for _ in range(m):
    a, b, c = input().split("\"")
    if b < 'Jane Eyre':
        heapq.heappush(friend, (int(a), b, int(c)))
print(friend)
time = 0
while pq:
    book, page = heapq.heappop(pq)
    time += page
    if book == 'Jane Eyre':
        break
    while friend and time >= friend[0][0]:
        t, b, p = heapq.heappop(friend)
        heapq.heappush(pq, (b, p))
print(time)
