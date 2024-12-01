from functools import cache
from collections import defaultdict

def solve(H):
    dep = defaultdict(list)
    op = defaultdict(list)
    val = defaultdict(int)
    ind = {}

    q = []
    qp = 0

    def calc(k):
        a, b, c = op[k]
        a = val[a]
        c = val[c]
        if b == '+':
            return a + c
        if b == '-':
            return a - c
        if b == '*':
            return a * c
        if b == '/':
            return a / c

    with open('in') as f:
        for i, l in enumerate(f.read().splitlines()):
            k = l[:4]
            if k == 'humn':
                val[k] = H
                q.append(k)
            else:
                try:
                    v = int(l[6:])
                    val[k] = v
                    q.append(k)
                except:
                    op[k] = l[6:].split(' ')
                    a, _, c = op[k]
                    ind[k] = 2
                    dep[a].append(k)
                    dep[c].append(k)

    while qp < len(q):
        k = q[qp]
        for x in dep[k]:
            ind[x] -= 1
            if ind[x] == 0:
                if x == 'root':
                    return val[op[x][0]] - val[op[x][2]]
                val[x] = calc(x)
                q.append(x)
        qp += 1

L, R = 0, 10**15
while L < R:
    mi = (L + R) // 2
    s = solve(mi)
    if s <= 0:
        R = mi
    else:
        L = mi + 1
print(L)