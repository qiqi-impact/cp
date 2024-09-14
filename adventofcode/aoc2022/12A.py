from collections import deque

board = []
i = 0
q = deque()
seen = set()

with open('in') as f:
    for l in f.read().splitlines():
        C = len(l)
        t = ''
        for j, c in enumerate(l):
            if c == 'S':
                t += 'a'
                q.append((0, i, j))
                seen.add((i, j))
            elif c == 'E':
                ed = (0, i, j)
                t += 'z'
            else:
                t += c
        board.append(t)
        i += 1
R = i
D = [[-1,0], [1, 0], [0, -1], [0, 1]]
found = False
while not found:
    c, x, y = q.popleft()
    for dx, dy in D:
        nx, ny = x+dx, y+dy
        if 0 <= nx < R and 0 <= ny < C:
            if (nx, ny) == (ed[1], ed[2]):
                print(c+1)
                found = True
                break
            elif ord(board[nx][ny]) - ord(board[x][y]) <= 1 and (nx, ny) not in seen:
                seen.add((nx, ny))
                q.append((c+1, nx, ny))