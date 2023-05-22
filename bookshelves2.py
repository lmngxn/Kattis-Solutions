from random import randint
from math import ceil

def shelves(S, M, L, shelf):
    if shelf % 6 == 0:
        result = ceil((S + M * 2 + L * 3)/shelf)
    elif shelf % 3 == 0:
        merge = min(S, M)
        L += merge
        S -= merge
        M -= merge
        result = L //(shelf // 3)
        L %= (shelf // 3)
        if M == 0:
            result += ceil((L * 3 + S) / shelf)
        elif S == 0:
            result += 1
            remainder = shelf - L * 3
            M -= remainder // 2
            result += ceil(M / (shelf // 2))
    elif shelf % 2 == 0:
        
    return result 


if __name__ == '__main__':
    while True:
        S = randint(0, 26)
        M = randint(0, 26 - S)
        L = randint(0, 26 - S - M)
        shelf = 7
        print(S, M, L, shelf)
        print(shelves(S, M, L, shelf))
        input()

