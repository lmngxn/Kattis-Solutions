from heapq import heappush
N = int(input())
street_people = list(map(int, input().split()))
total_people = street_people.copy()
M = int(input())
for _ in range(M):
    i, j = map(int, input().split())
    total_people[i-1] += street_people[j-1]
    total_people[j-1] += street_people[i-1]
rank = []
for i, p in enumerate(total_people):
    heappush(rank, (p, i+1))
print(rank[0][1])
