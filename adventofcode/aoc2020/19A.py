from functools import cache
from collections import defaultdict

val = {}
dep = defaultdict(list)
op = {}
ind = defaultdict(int)

q = []
qp = 0

def combine(s):
    l = [int(x) for x in s.split(' ')]
    ret = val[l[0]][:]
    for i in range(1, len(l)):
        nr = []
        c = val[l[i]][:]
        for x in ret:
            for y in c:
                nr.append(x + y)
        ret = nr
    return ret

def calc(s):
    if '|' in s:
        a, b = s.split(' | ')
        return combine(a) + combine(b)
    return combine(s)

stage = 0
ret = 0

with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        if len(l) == 0:
            stage += 1
            while qp < len(q):
                cur = q[qp]
                for x in dep[cur]:
                    ind[x] -= 1
                    if ind[x] == 0:
                        q.append(x)
                        val[x] = calc(op[x])
                qp += 1
            VALID = set(val[0])
            continue

        if stage == 0:
            a, b = l.split(': ')
            a = int(a)
            if b in ['"a"', '"b"']:
                val[a] = [b[1]]
                q.append(a)
            else:
                s = set()
                op[a] = b
                for x in b.split(' '):
                    try:
                        s.add(int(x))
                    except:
                        pass
                for k in s:
                    dep[k].append(a)
                    ind[a] += 1
        else:
            if l in VALID:
                ret += 1
print(ret)