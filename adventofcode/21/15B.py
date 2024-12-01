from functools import cache
from collections import defaultdict, deque, Counter
import itertools
import heapq
import math

ret = 0
RR = 0
board = []
with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        CC = len(l)
        RR += 1
        board.append([int(x) for x in l])

R, C = 5*RR, 5*CC

def get_board(i, j):
    diff = i//RR + j//CC
    return (board[i%RR][j%CC] + diff - 1) % 9 + 1

dist = {(0, 0): 0}
h = [(0, 0, 0)]
D = list(itertools.pairwise([-1, 0, 1, 0, -1]))

while h:
    c, x, y = heapq.heappop(h)
    if (x, y) == (R-1, C-1):
        print(c)
        break
    if (x, y) in dist and dist[x, y] < c:
        continue
    for dx, dy in D:
        nx, ny = x+dx, y+dy
        if 0 <= nx < R and 0 <= ny < C and ((nx, ny) not in dist or dist[nx, ny] > c + get_board(nx, ny)):
            dist[nx, ny] = c + get_board(nx, ny)
            heapq.heappush(h, (dist[nx, ny], nx, ny))
