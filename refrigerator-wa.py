# I purposely put the buggy live code shown at 8.23pm
# I said this is 'very' close to correct, and there are just two subtle bugs
# either figure out what's wrong or see the screenshot at class Discord

from math import inf, ceil
pa, ka, pb, kb, n = map(int, input().split())
ans, best_a, best_b = inf, -1, -1
for a in range(n+1):
    b = int(ceil((n - a*ka) // kb))
    # for b in range(n+1):
    if a*ka + b*kb >= n: # can
        cost = a*pa + b*pb
        if cost < ans:
            best_a, best_b, ans = a, b, cost
print(best_a, best_b, ans)
