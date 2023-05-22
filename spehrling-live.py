# Sperhling
# the final answer is omitted...

S1 = input()
S2 = input()
n, m = len(S1), len(S2)
# find i = length of common prefix of S1 and S2
i = 0
while i < n and i < m and S1[i] == S2[i]:
    i += 1
print(0) # think on how to use the value of i (length of common prefix of S1 and S2) to get the answer
