from functools import cache
from collections import defaultdict, deque
import math

def ints(s, split=' '):
    return [int(x) for x in s.split(split) if x]

def colon(s):
    return s.split(': ')[1]

def merge(l):
    return ''.join([str(x) for x in l])

digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digmap = {}
for i, x in enumerate(digits):
    digmap[x] = i

dirmap = {
    'R': [0, 1],
    'L': [0, -1],
    'U': [-1, 0],
    'D': [1, 0],
}
L, R, U, D = [[0,-1], [0,1], [-1,0], [1,0]]
DIR = [R, D, L, U]

lines = []
with open("in") as f:
    for a in f.read().splitlines():
        lines.append(a)
ln = len(lines)

NL, NH = 0, 0

class FF:
    def __init__(self):
        self.type = 'f'
        self.on = False
        self.out = []
        self.last_from = {}
    def proc(self, msg):
        if msg[2] == 0:
            self.on = not self.on
            return int(self.on)

class CON:
    def __init__(self):
        self.type = 'c'
        self.out = []
        self.last_from = {}
    def proc(self, msg):
        self.last_from[msg[0]] = msg[2]
        if sum(self.last_from.values()) == len(self.last_from):
            return 0
        else:
            return 1

class BRO:
    def __init__(self):
        self.type = 'b'
        self.out = []
        self.last_from = {}

class OUT:
    def __init__(self):
        self.type = 'o'
        self.out = []
        self.last_from = {}
    def proc(self, msg):
        return

m = {'rx': OUT()}

for l in lines:
    a, b = l.split(' -> ')
    bb = b.split(', ')
    if a[0] == 'b':
        m[a] = BRO()
        print(a)
    elif a[0] == '%':
        m[a[1:]] = FF()
    elif a[0] == '&':
        m[a[1:]] = CON()

for l in lines:
    a, b = l.split(' -> ')
    bb = b.split(', ')
    if a[0] == 'b':
        for x in bb:
            m[a].out.append(m[x])
            m[x].last_from[m[a]] = 0
    elif a[0] == '%':
        for x in bb:
            m[a[1:]].out.append(m[x])
            m[x].last_from[m[a[1:]]] = 0
    elif a[0] == '&':
        for x in bb:
            m[a[1:]].out.append(m[x])
            m[x].last_from[m[a[1:]]] = 0

for _ in range(1000):
    NL += 1
    q = deque([])
    for x in m['broadcaster'].out:
        q.append((m['broadcaster'], x, 0))
        NL += 1

    while q:
        msg = q.popleft()
        s, d, t = msg
        res = d.proc(msg)
        if res is not None:
            for x in d.out:
                q.append((d, x, res))
                if res:
                    NH += 1
                else:
                    NL += 1
print(NL*NH)