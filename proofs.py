from sys import stdin
true = set()
for i in range(int(stdin.readline())):
    assump, con = stdin.readline().split('->')
    if assump:
        for a in assump.split():
            if a not in true:
                print(i + 1)
                exit(0)
    true.add(con.strip())
print('correct')
