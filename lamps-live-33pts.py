# from here to get 100/100 is quite easy...
# just consider the case when you need more than one Incandescent bulb...

h, P = map(int, input().split())
for d in range(1, 8001): # just try all possible days, even if h == 1, so upperbound is 8000 days
    H = d*h
    Inc_cost = 5  + 60*H*P/100000
    Low_cost = 60 + 11*H*P/100000
    if Low_cost < Inc_cost:
        print(d)
        break
