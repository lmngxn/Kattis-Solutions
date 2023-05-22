lst = list(map(int, input().split()))

counter = 4
while lst != [1,2,3,4,5]:
    for i in range(counter):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            print(' '.join(str(x) for x in lst))
    counter -= 1

