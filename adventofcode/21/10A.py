from functools import cache
from collections import defaultdict, deque
import math
from itertools import pairwise

ret = 0
val = {
    ')': ['(', 3],
    ']': ['[', 57],
    '}': ['{', 1197],
    '>': ['<', 25137],
}
with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        st = []
        for c in l:
            if c in val:
                if not st or st[-1] != val[c][0]:
                    ret += val[c][1]
                    break
                else:
                    st.pop()
            else:
                st.append(c)
print(ret)