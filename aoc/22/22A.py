from functools import cache
from collections import defaultdict

board = []
pw = []

stage = 0
mxl = 0

with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        if len(l) == 0:
            stage = 1
            continue
        if stage == 1:
            cur = 0
            for c in l:
                if '0' <= c <= '9':
                    cur = 10 * cur + int(c)
                else:
                    if cur > 0:
                        pw.append(cur)
                    pw.append(c)
                    cur = 0
            if cur > 0:
                pw.append(cur)
        if stage == 0:
            board.append(l)
            mxl = max(mxl, len(l))

for i in range(len(board)):
    board[i] = board[i] + ((mxl - len(board[i])) * ' ')
# print(board)

# print(pw)

for j in range(mxl):
    if board[0][j] == '.':
        cx, cy = 0, j
        break

D = [[0, 1], [1, 0], [0, -1], [-1, 0]]
f = 0
R, C = len(board), len(board[0])
for op in pw:
    if op == 'R':
        f = (f+1)%4
    elif op == 'L':
        f = (f-1)%4
    else:
        print(cx, cy)
        dx, dy = D[f]
        for i in range(op):
            nx, ny = cx+dx, cy+dy
            if nx == R or (0 <= nx < R and 0 <= ny < C and f == 1 and board[nx][ny] == ' '):
                for i in range(R):
                    if board[i][ny] != ' ':
                        nx = i
                        break
            elif nx == -1 or (0 <= nx < R and 0 <= ny < C and f == 3 and board[nx][ny] == ' '):
                for i in range(R-1, -1, -1):
                    if board[i][ny] != ' ':
                        nx = i
                        break
            elif ny == C or (0 <= nx < R and 0 <= ny < C and f == 0 and board[nx][ny] == ' '):
                for i in range(C):
                    if board[nx][i] != ' ':
                        ny = i
                        break
            elif ny == -1 or (0 <= nx < R and 0 <= ny < C and f == 2 and board[nx][ny] == ' '):
                for i in range(C-1, -1, -1):
                    if board[nx][i] != ' ':
                        ny = i
                        break
            if board[nx][ny] == '#':
                break
            cx, cy = nx, ny
            print(cx, cy)
    
print(cx, cy, f)
print(1000 * (cx + 1) + 4 * (cy + 1) + f)