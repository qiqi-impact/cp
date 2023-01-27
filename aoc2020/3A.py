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

ret = 0
for i in range(R):
    j = 3*i%C
    if board[i][j] == '#':
        ret += 1

print(ret)