key = input()
memo = set(['q', ' '])
cipher = [['' for _ in range(5)] for _ in range(5)]
cipher_pos = dict()
counter = 0
for x in key:
    if x in memo:
        continue
    cipher[counter // 5][counter % 5] = x
    cipher_pos[x] = (counter // 5, counter % 5)
    memo.add(x)
    counter += 1
for i in range(97, 123):
    if chr(i) in memo:
        continue
    cipher[counter // 5][counter % 5] = chr(i)
    cipher_pos[chr(i)] = (counter // 5, counter % 5)
    counter += 1
    if counter >= 25:
        break
text = input().replace(' ', '')
counter = 0
encrypt = ''
while counter < len(text):
    first = text[counter]
    if counter == len(text) - 1 or text[counter + 1] == first:
        second = 'x'
        counter += 1
    else:
        second = text[counter + 1]
        counter += 2
    first_pos = cipher_pos[first]
    second_pos = cipher_pos[second]
    if first_pos[0] == second_pos[0]:
        encrypt += cipher[first_pos[0]][(first_pos[1] + 1) % 5] + cipher[second_pos[0]][(second_pos[1] + 1) % 5]
    elif first_pos[1] == second_pos[1]:
        encrypt += cipher[(first_pos[0] + 1) % 5][first_pos[1]] + cipher[(second_pos[0] + 1) % 5][second_pos[1]]
    else:
        encrypt += cipher[first_pos[0]][second_pos[1]] + cipher[second_pos[0]][first_pos[1]]
print(encrypt.upper())
