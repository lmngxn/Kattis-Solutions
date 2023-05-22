# there is a very tiny bug in this second last submission (scoring 90/100)
# understand the whole thing so that you can fix it

from statistics import median

N, t = map(int, input().split())
A = list(map(int, input().split()))
if t == 1:
    print(7)
elif t == 2:
    # if A[0] > A[1]:
    #     print("Bigger")
    # elif A[0] == A[1]:
    #     print("Equal")
    # else:
    #     print("Smaller")
    # DO NOT USE LINE 18 BELOW, CONFIRM FAIL IT5001 PE/Final <-- marks will be deducted, I am only showing off here...
    print("Bigger" if A[0] > A[1] else ("Equal" if A[0] == A[1] else "Smaller"))
elif t == 3:
    # DO NOT USE THIS, TOO COMPLICATED
    # if A[0] < A[1] < A[2]: # A[0], A[1], A[2], how many different arrangements
    #     print(A[1])
    # elif A[0] < A[2] < A[1]:
    #     print(A[2])
    # elif A[1] < A[0] < A[2]:
    #     print(A[0])
    # 3 more elif
    
    # A = sorted(A[:3]) # now this is correct
    # print(A[1])

    print(median(A[:3]))
elif t == 4:
    print(sum(A))
elif t == 5:
    print(sum([v for v in A if v%2 == 0])) # list comprehension
elif t == 6:
    print(''.join([chr(97+v%26) for v in A])) # chim
else:
    i = 0
    while A[i] != None:
        temp = A[i]
        A[i] = None
        i = temp
        if i < 0 or i > N-1:
            print("Out")
            break
        elif i == N-1:
            print("Done")
            break
    print("Cyclic")
