X = int(input())
counter = 0
factor = 2
while X != 1 and factor ** 2 < X:
    if X % factor == 0:
        X //= factor
        counter += 1
    else:
        factor += 1
if X == 1:
    print(counter)
elif factor ** 2 == X:
    print(counter + 2)
else:
    print(counter + 1)
