from math import ceil
n = int(input())
required = list(map(int, input().split()))
solved = list(map(int, input().split()))
computer = 1
total = 0

for limit, time in sorted(zip(solved, required)):
    if limit == -1:
        continue
    if ceil(time/limit) > computer:
        computer = ceil(time/limit)
    total += time
    if total / computer > limit:
        computer = ceil(total/limit)

print(computer)
    
