from functools import cache
from collections import defaultdict

board = []
pw = []

stage = 0
mxl = 0

# out of bounds x, y -> in bounds x, y and direction
tele = {}
stele = {}

stele[50, 100] = {0: [(49, 100), 3], 1: [(50, 99), 2]}
stele[99, 49] = {2: [(100, 49), 1], 3: [(99, 50), 0]}
stele[150, 50] = {1: [(150, 49), 2], 0: [(149, 50), 3]}

for i in range(50):
    # a0-an
    tele[150 + i, -1] = [(0, 50 + i), 1]
    tele[-1, 50 + i] = [(150 + i, 0), 0]

    #b0-bn
    tele[200, i] = [(0, 100 + i), 1]
    tele[-1, 100 + i] = [(199, i), 3]

    #c0-cn
    tele[150 + i, 50] = [(149, 50 + i), 3]
    tele[150, 50 + i] = [(150 + i, 49), 2]

    #d0-dn
    tele[49 - i, 150] = [(100 + i, 99), 2]
    tele[100 + i, 100] = [(49 - i, 149), 2]

    #e0-en
    tele[50, 100 + i] = [(50 + i, 99), 2]
    tele[50 + i, 100] = [(49, 100 + i), 3]

    #f0-fn
    tele[50 + i, 49] = [(100, i), 1]
    tele[99, i] = [(50 + i, 50), 0]

    #g0-gn
    tele[49 - i, 49] = [(100 + i, 0), 0]
    tele[100 + i, -1] = [(49 - i, 50), 0]

def prt(op):
    global cx, cy, f, mxl
    print((cx, cy), op)

    WINDOW_SIZE = 4
    print('='*(WINDOW_SIZE * 2 + 3))
    for i in range(cx - WINDOW_SIZE, cx + WINDOW_SIZE + 1):
        l = '|'
        for j in range(cy - WINDOW_SIZE, cy + WINDOW_SIZE + 1):
            if not (0 <= i < len(board) and 0 <= j < mxl) or board[i][j] == ' ':
                l += ' '
            elif (i, j) == (cx, cy):
                l += '>v<^'[f]
            else:
                l += board[i][j]
        l += '|'
        print(l)
    print('='*(WINDOW_SIZE * 2 + 3))
    input()

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
req = False
for op in pw:
    if op == 'R':
        f = (f+1)%4
    elif op == 'L':
        f = (f-1)%4
    else:
        dx, dy = D[f]
        nf = f
        for i in range(op):
            if req:
                # prt(op)
                req = False
            nx, ny = cx+dx, cy+dy
            pdx, pdy = dx, dy
            if (nx, ny) in stele:
                # prt(op)
                a, b = stele[nx, ny][f]
                nx, ny = a
                nf = b
                pdx, pdy = D[nf]
                req = True
                print((nx, ny))
            elif (nx, ny) in tele:
                # prt(op)
                a, b = tele[nx, ny]
                nx, ny = a
                nf = b
                pdx, pdy = D[nf]
                req = True
                print((nx, ny))
            if board[nx][ny] == '#':
                break
            cx, cy = nx, ny
            dx, dy = pdx, pdy
            f = nf
            # prt(op)
    
print(cx, cy, f)
print(1000 * (cx + 1) + 4 * (cy + 1) + f)