cases = int(input())
for _ in range(cases):
    p = input()
    end = int(input())
    lst = input()[1:-1].split(',')
    order = 1
    start = 0
    for x in p:
        if x == 'R':
            order *= -1
        elif x == 'D':
            if order == 1:
                start += 1
            else:
                end -= 1
        if end < start:
            break
    if end < start:
        print('error')
    elif order == 1:
        print('[' + ','.join(lst[start:end]) + ']')
    elif order == -1:
        if start == 0:
            print('[' + ','.join(lst[end-1::-1]) + ']')
        else:
            print('[' + ','.join(lst[end-1:start-1:-1]) + ']')
