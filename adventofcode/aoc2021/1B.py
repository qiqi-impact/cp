from functools import cache
from collections import defaultdict, deque
import math

ret = 0
arr = []
with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        arr.append(int(l))

cur = 1e9
for i in range(2, len(arr)):
    x = sum(arr[i-2:i+1])
    if x > cur:
        ret += 1
    cur = x

print(ret)