from functools import cache
from collections import defaultdict, deque, Counter
import itertools
import heapq
import math
import re
import json

R = 0
board = []
with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        R += 1
        C = len(l)
        board.append(l)

q = 1
for dx, dy in [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]:
    ret = 0
    for i in range(0, R, dx):
        j = dy*i//dx%C
        if board[i][j] == '#':
            ret += 1
    q *= ret
print(q)