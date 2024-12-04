from functools import cache
from collections import defaultdict, deque
import math
from itertools import pairwise

ret = []
val = {
    ')': ['(', 3],
    ']': ['[', 57],
    '}': ['{', 1197],
    '>': ['<', 25137],
}
rv = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}
with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        st = []
        fail = False
        for c in l:
            if c in val:
                if not st or st[-1] != val[c][0]:
                    fail = True
                    break
                else:
                    st.pop()
            else:
                st.append(c)
        if not fail:
            cur = 0
            for i in range(len(st)-1, -1, -1):
                cur *= 5
                cur += rv[st[i]]
            ret.append(cur)
ret.sort()
print(ret[len(ret)//2])