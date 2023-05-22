# this one is not correct
# think of how to use variable 'wasted' to get the correct answer

from math import inf
K = int(input())
ans = inf
for a in range(K//500 + 1 + 1): # just try a, a is all possible topups of 500 SEK
    for b in range(K//200 + 1 + 1): # just try b, b is all possible topups of 200 SEK
        for c in range(K//100 + 1 + 1): # just try c, c is all possible topups of 100 SEK
            amt = a*500+b*200+c*100
            num_transactions = a+b+c
            wasted = amt-K
            if amt >= K and num_transactions < ans:
                # print(a, b, c, a*500+b*200+c*100, K)
                ans = num_transactions
print(ans)
