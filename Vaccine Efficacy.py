vac = [0, 0, 0, 0]
control = [0, 0, 0, 0]

for _ in range(int(input())):
    person = input()
    if person[0] == 'N':
        control[0] += 1
        for i in range(1,4):
            if person[i] == 'Y':
                control[i] += 1
    else:
        vac[0] += 1
        for i in range(1,4):
            if person[i] == 'Y':
                vac[i] += 1


for i in range(1,4):
    if vac[i]/vac[0] >= control[i]/control[0]:
        print('Not Effective')
    else:
        print(f'{(control[i]/control[0] - vac[i]/vac[0])/(control[i]/control[0])*100:.6f}')
