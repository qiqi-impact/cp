from functools import cache
from collections import defaultdict, deque, Counter
import math

d = defaultdict(int)
ALPHA = 'abcdefg'
sets = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

ret = 0
with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        a, b = l.split(' | ')
        m = {}
        ct = Counter()
        q = a.split(' ')
        q.sort(key=len)
        amt = 0
        for x in q:
            ct += Counter(x)
        for w in q:
            if len(w) == 2:
                x, y = w[0], w[1]
                if ct[x] == 8:
                    m[x] = 'c'
                    m[y] = 'f'
                else:
                    m[x] = 'f'
                    m[y] = 'c'
            elif len(w) == 3:
                s = set(w) - set(q[0])
                m[s.pop()] = 'a'
            elif len(w) == 4:
                l = [c for c in w if c not in m]
                x, y = l[0], l[1]
                if ct[x] == 6:
                    m[x] = 'b'
                    m[y] = 'd'
                else:
                    m[x] = 'd'
                    m[y] = 'b'
            elif len(w) == 6:
                l = [c for c in w if c not in m]
                if len(l) == 1:
                    m[l[0]] = 'g'
                    for x in ALPHA:
                        if x not in m:
                            m[x] = 'e'
        for w in b.split(' '):
            t = ''.join(sorted([m[c] for c in w]))
            amt *= 10
            amt += sets.index(t)
        print(amt)
        ret += amt
print(ret)