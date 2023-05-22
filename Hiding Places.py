n = int(input())
def move(r, c):
    moves = [(r+2, c-1), (r+2, c+1), (r+1, c-2), (r+1, c+2), (r-1, c-2), (r-1, c+2),(r-2, c-1), (r-2, c+1)]
    result = []
    for r, c in moves:
        if 0<=r<8 and 0<=c<8 and (r,c) not in visited:
            result.append((r,c))
            visited.add((r,c))
    return result

for _ in range(n):
    start = input()
    start = (8 - int(start[1]), ord(start[0]) - 97)
    visited = set()
    visited.add(start)
    next_frontier = [(start)]
    counter = 1
    while len(visited) < 64:
        frontier = next_frontier
        next_frontier = []
        for r, c in frontier:
            next_frontier.extend(move(r, c))
        counter += 1
    print(counter - 1, end = ' ')
    next_frontier.sort(key = lambda element : element[1])
    next_frontier.sort()
    for r, c in next_frontier:
        print(f'{chr(c+97)}{8-r} ', end = '')
    print('')
