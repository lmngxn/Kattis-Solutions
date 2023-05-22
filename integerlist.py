#Matric No.: A0002533Y
#Name: Lee Ming Xuan
#Lab: B2

from collections import deque

cases = int(input())
for _ in range(cases):
    p = input()
    n = int(input())
    lst = deque(input()[1:-1].split(','))
    order = 1
    for c in p:
        if c == 'R':
            order *= -1
        elif c == 'D' and n == 0:
            n -= 1
            break
        elif c == 'D' and order == 1:
            lst.popleft()
            n -= 1
        elif c == 'D' and order == -1:
            lst.pop()
            n -= 1
    if n < 0:
        print('error')
    else:
        if order == -1:
            lst.reverse()
        print('[' + ','.join(lst) + ']')
        
            
