"""

n = int(input())
stack = []
for card in input().split():
    if not stack:
        stack.append(int(card)%2)
    elif int(card)%2 == stack[-1]:
        stack.pop()
        n -= 2
    else:
        stack.append(int(card)%2)
print(n)            
"""

n = int(input())
cards = input().split()
stack = []
remaining = 0
counter = 0
while counter < n:
    if counter != n - 1 and int(cards[counter]) % 2 == int(cards[counter+1]) % 2:
        counter += 2
    elif remaining and int(cards[counter]) % 2 == stack[-1]:
        counter += 1
        remaining -= 1
        stack.pop()
    else:
        stack.append(int(cards[counter]) % 2)
        remaining += 1
        counter += 1
print(remaining)      
