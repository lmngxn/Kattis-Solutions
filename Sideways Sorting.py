r, c = map(int, input().split())
result = []

while r and c:
    lst = [''] * c
    for _ in range(r):
        line = input()
        for i in range(c):
            lst[i] += line[i]
    lst = sorted(lst, key = lambda x: x.lower())
    case = [''] * r
    for i in range(r):
        for j in range(c):
            case[i] += lst[j][i]
    result.append(case)
    r, c = map(int, input().split())
    
for case in result:
    for x in case:
        print(x)
    print()
