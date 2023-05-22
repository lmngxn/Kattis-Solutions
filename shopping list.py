n, m = map(int, input().split())
same_items = set(input().split())
for _ in range(n - 1):
    same_items = same_items.intersection(set(input().split()))
print(len(same_items))
print(*sorted(same_items), sep = '\n')
