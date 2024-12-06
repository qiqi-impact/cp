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

lines = []
step = 0
rules = defaultdict(set)
ret = 0
with open("in") as f:
    for a in f.read().splitlines():
        lines.append(a)
        if step == 0:
            if a == '':
                step = 1
            else:
                x, y = ints(a, '|')
                rules[x].add(y)
        else:
            l = ints(a, ',')
            r = 1
            for i in range(len(l)):
                for j in range(i+1, len(l)):
                    if l[i] in rules[l[j]]:
                        r = 0
            if not r:
                ind = defaultdict(int)
                for i in range(len(l)):
                    for j in range(i+1, len(l)):
                        if l[i] in rules[l[j]]:
                            ind[l[i]] += 1
                        if l[j] in rules[l[i]]:
                            ind[l[j]] += 1
                q = deque()
                s = []
                for x in l:
                    if ind[x] == 0:
                        q.append(x)
                        s.append(x)
                while q:
                    cur = q.popleft()
                    for t in rules[cur]:
                        ind[t] -= 1
                        if ind[t] == 0:
                            q.append(t)
                            s.append(t)
                ret += s[len(s)//2]
print(ret)
        

ln = len(lines)