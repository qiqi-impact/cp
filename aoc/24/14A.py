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

dirmap = {
    'R': [0, 1],
    'L': [0, -1],
    'U': [-1, 0],
    'D': [1, 0],
}
L, R, U, D = [[0,-1], [0,1], [-1,0], [1,0]]
DIR = [R, D, L, U]

lines = []

ct = [0,0,0,0]

H, W = 103, 101
# H, W = 7, 11

def prt(s):
    for i in range(H):
        for j in range(W):
            if (i, j) in s:
                print('#',end='')
            else:
                print(' ',end='')
        print()
    print()


def maybe(s):
    for (x, y) in s:
        # if x + y <= W // 10 or (W - y) + x <= W // 10:
        #     return False
        for dx in [-1, 1]:
            for dy in [0]:
                for j in range(1, 2):
                    r = 1
                    for i in range(3):
                        if (x+dx*i*j, y+dy*i*j) not in s:
                            r = 0
                            break
                    if r:
                        return True
    return False

ss = set()

with open("in") as f:
    for a in f.read().splitlines():
        t, y = a.split(' ')
        l = t.split('=') + y.split('=')
        p, v = l[1].split(','), l[3].split(',')
        # print(p, v)
        y, x = int(p[0]), int(p[1])
        vy, vx = int(v[0]), int(v[1])
        # print(x, y, vx, vy)
        ss.add((x, y))
    

    ct = 0
    while 1:
        if ct % 1000 == 0:
            print(ct)
        if maybe(ss):
            prt(ss)
            print(ct)
            input()
            
        ct += 1

        nss = set()
        for x, y in ss:
            tx = (x + 1 * vx) % H
            ty = (y + 1 * vy) % W
            nss.add((tx, ty))
        ss = nss

        # a = H // 2 - tx
        # b = W // 2 - ty
        # # print(a, b)

        # if a < 0 and b < 0: ct[0] += 1
        # if a > 0 and b < 0: ct[1] += 1
        # if a < 0 and b > 0: ct[2] += 1
        # if a > 0 and b > 0: ct[3] += 1
        # print(ct)

# print(ct[0] * ct[1] * ct[2] * ct[3])
