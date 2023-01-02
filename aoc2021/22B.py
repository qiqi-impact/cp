from functools import cache
from collections import defaultdict, deque, Counter
import itertools
import heapq
import math
import re

ev = {}

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