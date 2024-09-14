from functools import cache
from collections import defaultdict, deque
import math


def val(d):
    return '=-012'.find(d) - 2

ret = 0
with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        cur = 0
        for c in l:
            cur = 5 * cur + val(c)
        ret += cur

print(ret)

l = []
while ret:
    q = ret % 5
    c = '=-012'[(q+2)%5]
    l.append(c)
    ret -= (q+2)%5 - 2
    ret //= 5
print(''.join(l[::-1]))