from functools import cache
from collections import defaultdict, deque, Counter
import itertools
import heapq
import math
import re

p = []
lit = set()

with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        ll = re.split(' |=|\.\.|,', l)
        b = ll[0] == 'on'
        t = []
        for x in ll:
            try:
                t.append(int(x))
            except:
                pass
        
        t[0] = max(t[0], -50)
        t[1] = min(t[1], 50)
        t[2] = max(t[2], -50)
        t[3] = min(t[3], 50)
        t[4] = max(t[4], -50)
        t[5] = min(t[5], 50)

        if b:
            for x in range(t[0], t[1]+1):
                for y in range(t[2], t[3]+1):
                    for z in range(t[4], t[5]+1):
                        lit.add((x, y, z))
        else:
            for x in range(t[0], t[1]+1):
                for y in range(t[2], t[3]+1):
                    for z in range(t[4], t[5]+1):
                        lit.discard((x, y, z))

print(len(lit))