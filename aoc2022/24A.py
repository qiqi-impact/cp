from functools import cache
from collections import defaultdict, deque
import math

board = []

blizzards = defaultdict(list)

D = [[0, 1], [1, 0], [0, -1], [-1, 0]]

class Bliz:
    def __init__(self, dir, x, y):
        self.dir = dir
        self.x, self.y = x, y
    def move(self):
        nx, ny = self.x + D[self.dir][0], self.y + D[self.dir][1]
        if board[nx][ny] == '#':
            if self.dir == 0:
                ny = 1
            elif self.dir == 1:
                nx = 1
            elif self.dir == 2:
                ny = C-2
            else:
                nx = R-2
        self.x, self.y = nx, ny

with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        x = []
        for j, c in enumerate(l):
            x.append(c)
            if c in '>v<^':
                blizzards[i,j].append(Bliz('>v<^'.find(c), i, j))
        board.append(x)

R, C = len(board), len(board[0])
T = math.lcm(R-2, C-2)

squares = []
for t in range(T):
    squares.append(set(blizzards.keys()))
    nb = defaultdict(list)
    for (x, y) in blizzards:
        for b in blizzards[x, y]:
            b.move()
            nb[b.x, b.y].append(b)
    blizzards = nb

memo = {
    (0, 1, 0): 0,
}

q = deque([(0, 1, 0)])
win = False
while q:
    x, y, t = q.popleft()
    nt = (t+1)%T
    for dx, dy in D + [[0, 0]]:
        nx, ny = x+dx, y+dy
        if (nx, ny, nt) not in memo and 0 <= nx < R and 0 <= ny < C and board[nx][ny] != '#' and (nx, ny) not in squares[nt]:
            q.append((nx, ny, nt))
            memo[nx, ny, nt] = memo[x, y, t] + 1
            if (nx, ny) == (R-1, C-2):
                print(memo[nx, ny, nt])
                win = True
                break
    if win:
        break
