n, m = map(int, input().split())
if m < n - 1 or m > 2 * n - 3:
    print('-1')
    exit(0)
bus = []
for i in range(2, n + 1):
    bus.append(f'{1} {i}')
for i in range(2, m - n + 3):
    bus.append(f'{n} {i}')
print(*bus, sep = '\n')
