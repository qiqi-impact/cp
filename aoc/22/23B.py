from functools import cache
from collections import defaultdict

DIR = [
    [[-1, -1], [-1, 0], [-1, 1]],
    [[1, -1], [1, 0], [1, 1]],
    [[-1, -1], [0, -1], [1, -1]],
    [[-1, 1], [0, 1], [1, 1]],
]
dp = 0

elves = []
s = set()

R = 0
with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        R += 1
        for j in range(len(l)):
            if l[j] == '#':
                elves.append((i, j))
        C = len(l)
s = set(elves)

mnx = mny = mxx = mxy = None
def prt():
    global mnx, mny, mxx, mxy
    for i in range(mnx, mxx+1):
        l = ''
        for j in range(mny, mxy+1):
            if (i, j) in s:
                l += '#'
            else:
                l += '.'
        print(l)
    print()

# prt()

turn = 1
while 1:
    ne = []
    prop = []
    pf = defaultdict(int)
    for i, (x, y) in enumerate(elves):
        ct = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = x+dx, y+dy
                if (nx, ny) in s:
                    ct += 1
        if ct == 1:
            p = (x, y)
            prop.append(p)
            pf[p] += 1
            continue
        for d in range(dp, dp+4):
            da = DIR[d%4]
            fail = False
            for dx, dy in da:
                nx, ny = x+dx, y+dy
                if (nx, ny) in s:
                    fail = True
                    break
            if not fail:
                p = (x+da[1][0], y+da[1][1])
                prop.append(p)
                pf[p] += 1
                break
        if len(prop) < i+1:
            p = (x, y)
            prop.append(p)
            pf[p] += 1
    # print(len(prop), len(elves))
    for i, (x, y) in enumerate(elves):
        if pf[prop[i]] == 1:
            ne.append(prop[i])
        else:
            ne.append((x, y))
    elves = ne
    ss = set(elves)
    if ss == s:
        print(turn)
        break
    s = ss
    dp = (dp+1)%4

    mnx = mny = 1e9
    mxx = mxy = -1e9
    for x, y in s:
        mnx = min(mnx, x)
        mxx = max(mxx, x)
        mny = min(mny, y)
        mxy = max(mxy, y)
    turn += 1

    # prt()


# print((mxy - mny + 1) * (mxx - mnx + 1) - len(s))