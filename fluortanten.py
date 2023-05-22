n = int(input())
lst = list(map(int, input().split()))

lst.pop(lst.index(0))
result = sum((i + 2) * x for i, x in enumerate(lst))
check = result
for x in lst:
    check -= x
    if check > result:
        result = check

print(result)
