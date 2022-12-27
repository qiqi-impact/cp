from functools import cache
from collections import defaultdict, deque
import math

ct = 0

boards = []
solved = []

with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        if ct == 0:
            order = [int(x) for x in l.split(',')]
        elif ct % 6 == 1:
            boards.append([])
            solved.append(False)
        else:
            q = []
            for x in l.split(' '):
                if len(x):
                    q.append([int(x), False])
            boards[-1].append(q)
        ct += 1

def check_all_boards():
    ret = []
    for k, b in enumerate(boards):
        if solved[k]:
            continue
        for i in range(5):
            t = 0
            for j in range(5):
                if b[i][j][1]:
                    t += 1
            if t == 5:
                ret.append(k)
        for j in range(5):
            t = 0
            for i in range(5):
                if b[i][j][1]:
                    t += 1
            if t == 5:
                ret.append(k)
    ret = list(set(ret))
    return ret

def unmarked(idx):
    b = boards[idx]
    ret = 0
    for i in range(5):
        for j in range(5):
            if not b[i][j][1]:
                ret += b[i][j][0]
    return ret

need = len(boards)
last = None
for x in order:
    for b in boards:
        for i in range(5):
            for j in range(5):
                if b[i][j][0] == x:
                    b[i][j][1] = True
    l = check_all_boards()
    print(l)
    for idx in l:
        solved[idx] = True
        need -= 1
        last = idx
    if need == 0:
        print(unmarked(last) * x)
        break