n = int(input())
DOM_results = {}
DOM_list = sorted([input() for _ in range(n)])
Kattis_list = sorted([input() for _ in range(n)])
D_counter = 0
K_counter = 0
result = 0
while D_counter < n and K_counter < n:
    if DOM_list[D_counter] == Kattis_list[K_counter]:
        D_counter += 1
        K_counter += 1
        result += 1
    elif DOM_list[D_counter] < Kattis_list[K_counter]:
        D_counter += 1
    elif Kattis_list[K_counter] < DOM_list[D_counter]:
        K_counter += 1
print(result)
