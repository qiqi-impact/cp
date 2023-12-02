from functools import cache
from collections import defaultdict, deque, Counter
import itertools
import heapq
import math
import re
import json

s = set(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt'])

ret = 0
with open("in") as f:
    
    for x in f.read().splitlines():
        if x == '':
            if len(s) == 0:
                ret += 1
            s = set(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'])
        else:
            for t in x.split(' '):
                q = t.split(':')
                s.discard(q[0])
    if len(s) == 0:
        ret += 1
    print(ret)