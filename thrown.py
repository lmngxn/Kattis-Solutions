n, k = map(int, input().split())
commands = input().split()
result = []
counter = 0
while k > 0:
    if commands[counter] == 'undo':
        for _ in range(int(commands[counter+1])):
            result.pop()
        counter += 2
    else:
        result.append(int(commands[counter]))
        counter += 1
    k -= 1
print(sum(result)%n)
