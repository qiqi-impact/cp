from functools import cache
from collections import defaultdict, deque, Counter
import itertools
import heapq
import math
import re
import json

l = []
with open("in") as f:
    for a in f.read().splitlines():
        x, y = a.split(' ')
        y = int(y)
        l.append([x, y])

def sim():
    s = set()
    cur = 0
    acc = 0
    while 1:
        if cur in s:
            return False, 0
        if cur == len(l):
            return True, acc
        s.add(cur)
        x, y = l[cur]
        if x == 'acc':
            acc += y
            cur += 1
        elif x == 'nop':
            cur += 1
        else:
            cur += y

for i in range(len(l)):
    if l[i][0] == 'jmp':
        l[i][0] = 'nop'
        a, b = sim()
        if a:
            print(b)
            break
        l[i][0] = 'jmp'
    elif l[i][0] == 'nop':
        l[i][0] = 'jmp'
        a, b = sim()
        if a:
            print(b)
            break
        l[i][0] = 'nop'

    