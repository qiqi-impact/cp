from functools import cache
from collections import defaultdict, deque, Counter
import itertools
import heapq
import math
import re, json

right = set()
down = set()

R = 0
with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        C = len(l)
        R += 1
        for j, c in enumerate(l):
            if c == 'v':
                down.add((i, j))
            elif c == '>':
                right.add((i, j))
    
for step in range(100000000):
    new_right = set()
    new_down = set()
    d = 0

    for (x, y) in right:
        ny = (y + 1)%C
        if (x, ny) not in right and (x, ny) not in down:
            new_right.add((x, ny))
        else:
            new_right.add((x, y))
    if right == new_right:
        d += 1
    right = new_right

    for (x, y) in down:
        nx = (x + 1)%R
        if (nx, y) not in right and (nx, y) not in down:
            new_down.add((nx, y))
        else:
            new_down.add((x, y))
    if down == new_down:
        d += 1
    down = new_down

    if d == 2:
        print(step+1)
        break