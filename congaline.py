N, Q = map(int, input().split())
class Node:
    def __init__(self, value = None, partner = None, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev
        self.partner = partner

class DDL:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

    def appendC(self, node):
        if node.partner == line.tail:
            self.append(node)
        else:
            node.next = node.partner.next
            node.next.prev = node
            node.partner.next = node
            node.prev = node.partner
            
    def pop(self, node):
        if node == self.head:
            self.head = node.next
            node.next.prev = node.next = None
        else:   
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = node.prev = None
        return node

    def print(self):
        temp = self.head
        while temp != self.tail:
            print(temp.value)
            temp = temp.next
        print(temp.value)

line = DDL()
for i in range(N):
    c1, c2 = input().split()
    node1 = Node(value = c1)
    node2 = Node(value = c2)
    node1.partner = node2
    node2.partner = node1
    line.append(node1)
    line.append(node2)

instructions = input()
mic = line.head
for x in instructions:
    if x == 'F':
        mic = mic.prev
    elif x == 'B':
        mic = mic.next
    elif x == 'R':
        if mic == line.tail:
            mic = line.head
        else:
            temp = mic.next
            line.append(line.pop(mic))
            mic = temp
    elif x == 'C':
        if mic == line.tail:
            mic = line.head
        else:
            temp = mic.next
            line.appendC(line.pop(mic))
            mic = temp
    elif x == 'P':
        print(mic.partner.value)

print('')
line.print()
