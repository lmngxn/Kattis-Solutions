from collections import defaultdict
from sys import stdin
N = int(stdin.readline())
full_var = defaultdict(lambda:["UNDECLARED"])
var_depth = defaultdict(set)
depth = 0
for _ in range(N):
    action, *obj = stdin.readline().split()
    if action == '{':
        depth += 1

    if action == '}':
        for var in var_depth[depth]:
            full_var[var].pop()
        var_depth[depth].clear()
        depth -= 1
        
    if action == 'DECLARE':
        if obj[0] not in var_depth[depth]:
            full_var[obj[0]].append(obj[1])
            var_depth[depth].add(obj[0])
        else:
            print('MULTIPLE DECLARATION')
            exit(0)

    if action == 'TYPEOF':
        print(full_var[obj[0]][-1])


    
