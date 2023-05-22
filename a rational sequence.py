P = int(input())
memo = dict()
def search(n):
    if n == 1:
        return 1, 1
    if n % 2:
        if n//2 not in memo:
            memo[n//2] = search(n//2)
        return sum(memo[n//2]), memo[n//2][1] 
    else:
        if n//2 not in memo:
            memo[n//2] = search(n//2)
        return memo[n//2][0], sum(memo[n//2])

for _ in range(P):
    k, n = input().split()
    p, q = search(int(n))
    print(f'k {p}/{q}')
