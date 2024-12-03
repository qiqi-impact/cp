from functools import cache
from collections import defaultdict, deque
import math

def ints(s, split=' '):
    return [int(x) for x in s.split(split) if x]

def grabint(s, idx):
    cur = 0
    ln = 0
    for i in range(idx, len(s)):
        try:
            cur = 10 * cur + int(s[i])
        except:
            return cur, i
    return cur, len(s)

def colon(s):
    return s.split(': ')[1]

def merge(l):
    return ''.join([str(x) for x in l])

digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digmap = {}
for i, x in enumerate(digits):
    digmap[x] = i

lines = []
ret = 0
m = 1
with open("in") as f:
    t, y = [], []
    ct = {}
    for a in f.read().splitlines():
        for i in range(3, len(a)):
            if a[i-3:i+1] == 'do()':
                m = 1
            elif i >= 6 and a[i-6:i+1] == 'don\'t()':
                m = 0
            elif a[i-3:i+1] == 'mul(':
                x, idx = grabint(a, i+1)
                if idx == i+1 or a[idx] != ',':
                    continue
                y, t = grabint(a, idx+1)
                if t == idx + 1 or t >= len(a) or a[t] != ')':
                    continue
                ret += x * y * m
print(ret)


