from random import randint
from math import ceil

def shelves(S, M, L, shelf):
    result = 0
    if L:
        result += L//(shelf//3)
        L %= (shelf//3)
        
        if shelf % 3 == 2:
            M -= result
        elif shelf % 3 == 1:
            S -= result

    if L:
        result += 1
        remainder = shelf - L * 3
        M -= remainder // 2
        remainder %= 2
        if remainder:
            S -= 1

    if M < 0:
        S += M * 2
        M = 0

    if M:
        result_M = M//(shelf//2)
        result += result_M
        M %= (shelf//2)
        if shelf % 2 == 1:
            S -= result_M

    if M:
        result += 1
        S -= shelf - M * 2
        M = 0
        
    if S > 0:
        result += ceil(S/shelf)

    return result 


if __name__ == '__main__':
    while True:
        S = randint(0, 26)
        M = randint(0, 26 - S)
        L = randint(0, 26 - S - M)
        shelf = 8
        print(S, M, L, shelf)
        print(shelves(S, M, L, shelf))
        input()

