str = input()
result = []
for x in str:
    if x == '<':
        result.pop(-1)
    else:
        result.append(x)
print(''.join(result))
