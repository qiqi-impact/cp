from functools import cache
from collections import defaultdict, deque, Counter
import math

ret = 0
stage = 0
rules = {}
with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        if len(l) == 0:
            stage += 1
            continue
        if stage == 0:
            s = l
        if stage == 1:
            a, b = l.split(' -> ')
            rules[a] = b

for _ in range(10):
    ns = s[0]
    for i in range(len(s)-1):
        x = s[i:i+2]
        if x in rules:
            ns += rules[x]
        ns += s[i+1]
    s = ns

ct = Counter(s)
print(max(ct.values()) - min(ct.values()))