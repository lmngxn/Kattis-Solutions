N = int(input())
for i in range(N):
    _ = int(input())
    memo = set()
    for C in input().split():
        if C in memo:
            memo.remove(C)
        else:
            memo.add(C)
    for C in memo:
        print(f'Case #{i+1}: {C}')
