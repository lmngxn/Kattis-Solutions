from math import ceil

def total_cost(pa, ka, pb, kb, n, xa):
    xb = ceil((n - (xa * ka)) / kb)
    return pa * xa + pb * xb

def fridge(pa, ka, pb, kb, n):
    all_cost = []
    trips_a = ceil(n / ka)
    for i in range(trips_a + 1):
        all_cost.append(total_cost(pa, ka, pb, kb, n, i))

    trips_a = all_cost.index(min(all_cost))
    trips_b = ceil((n - (trips_a * ka)) / kb)
    print(f'{trips_a} {trips_b} {all_cost[trips_a]}')

    max_a = ceil(n / ka)
    all_cost = [0 for _ in range(max_a + 1)]
    current_a = max_a
    all_cost[current_a] = current_cost = total_cost(pa, ka, pb, kb, n, current_a)
    next_cost = total_cost(pa, ka, pb, kb, n, current_a - 1)
    while next_cost < current_cost:
        current_a -= 1
        all_cost[current_a] = current_cost = next_cost
        next_cost = total_cost(pa, ka, pb, kb, n, current_a - 1)
    min_cost = current_cost
    current_a = 0
    all_cost[current_a] = current_cost = total_cost(pa, ka, pb, kb, n, current_a)
    next_cost = total_cost(pa, ka, pb, kb, n, current_a + 1)
    while next_cost < current_cost:
        current_a += 1
        all_cost[current_a] = current_cost = next_cost
        next_cost = total_cost(pa, ka, pb, kb, n, current_a + 1)
    if min_cost > current_cost:
        min_cost = current_cost
    final_a = all_cost.index(min_cost)
    final_b = ceil((n - (final_a * ka)) / kb)
    print(f'{final_a} {final_b} {min_cost}')     

pa, ka, pb, kb, n = (500, 10, 526, 11, 210)
