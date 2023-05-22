N = int(input())
lst = sorted(list(map(int, input().split())))
Q = int(input())
for _ in range(Q):
    start, end = map(int, input().split())
    if start > lst[-1]:
        print(0)
        continue
    if end < lst[0]:
        print(0)
        continue
    if start <= lst[0] and end >= lst[-1]:
        print(N)
        continue
    if start <= lst[0]:
        start_i = 0
    else:
        low = 0
        high = N-1
        while lst[low] <= start <= lst[high]:
            if low + 1 == high:
                start_i = high
                break
            check = (high + low)//2
            if lst[check] == start:
                while lst[check - 1] == start:
                    check -= 1
                    if check == 0:
                        break
                start_i = check
                break
            elif lst[check] > start:
                high = check
            elif lst[check] < start:
                low = check
    if end >= lst[-1]:
        end_i = N-1
    else:
        low = 0
        high = N-1
        while lst[low] <= end <= lst[high]:
            if low + 1 == high:
                end_i = low
                break
            check = (high + low)//2
            if lst[check] == end:
                while lst[check + 1] == end:
                    check += 1
                    if check == N - 1:
                        break
                end_i = check
                break
            elif lst[check] > end:
                high = check
            elif lst[check] < end:
                low = check
    result = end_i - start_i + 1
    print(result)
