num = int(input())
for i in range(num):
    recording = input().split()
    sounds = set()
    check = input()
    while check != 'what does the fox say?':
        sounds.add(check.split()[-1])
        check = input()
    print(' '.join(filter(lambda x:x not in sounds, recording)))
