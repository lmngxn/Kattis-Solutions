n = int(input())
result = []

while n:
    lst = [input() for _ in range(n)]
    result.append(sorted(lst, key= lambda x: x[:2]))
    n = int(input())
    
for case in result:
    for x in case:
        print(x)
    print()
