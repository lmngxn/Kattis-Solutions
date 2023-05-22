N, T = map(int, input().split())
lst = [int(input()) for _ in range(N)]
lst.sort(reverse = True)

def test(lst):
    counter = len(lst)
    for x in lst:
        if x < counter * T:
            return False
        counter -= 1
    return True

if test(lst):
    print('YES')
else:
    print('NO')
