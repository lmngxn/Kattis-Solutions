from collections import defaultdict
from sys import stdin
first = stdin.readline().strip()
n = int(stdin.readline())
letters = defaultdict(list)
for _ in range(n):
    word = stdin.readline().strip()
    letters[word[0]].append(word)
if first[-1] in letters:
    for word in letters[first[-1]]:
        if word[-1] not in letters or letters[word[-1]] == [word]:
            print(word + '!')
            exit(0)
    print(letters[first[-1]][0])
else:
    print('?')
