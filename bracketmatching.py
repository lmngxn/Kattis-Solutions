n = int(input())
line = input()
stack = []
left_bracket = {'(', '[', '{'}
right_bracket = {')', ']', '}'}
validity = True
for i in range(n):
    if line[i] in left_bracket:
        stack.append(line[i])
    elif line[i] in right_bracket:
        if not stack:
            validity = False
        elif line[i] == ')':
            validity = ('(' == stack.pop())
        elif line[i] == ']':
            validity = ('[' == stack.pop())
        elif line[i] == '}':
            validity = ('{' == stack.pop())
    if not validity:
        break
if stack:
    validity = False
print('Valid' if validity else 'Invalid')
