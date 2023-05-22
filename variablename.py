from collections import defaultdict
from sys import stdin
N = int(stdin.readline())
taken = defaultdict(lambda:1)
memo = set()
for _ in range(N):
    c = int(stdin.readline())
    if c in memo:
        while c * taken[c] in memo:
            taken[c] += 1
        c *= taken[c]
    else:
        taken[c] = 2
    memo.add(c)
    print(c)
