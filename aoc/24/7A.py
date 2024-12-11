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


def dfs(sm, cur, idx, ll):
    if idx == len(ll):
        return sm == cur
    if cur + ll[idx] <= sm:
        if dfs(sm, cur + ll[idx], idx + 1, ll):
            return True
    if cur * ll[idx] <= sm:
        if dfs(sm, cur * ll[idx], idx + 1, ll):
            return True
    if int(str(cur)+str(ll[idx])) <= sm:
        if dfs(sm, int(str(cur)+str(ll[idx])), idx + 1, ll):
            return True
    return False


lines = []
ret = 0
with open("in") as f:
    for a in f.read().splitlines():
        # lines.append(a)
        s, l = a.split(': ')
        s = int(s)
        l = ints(l)
        if dfs(s, l[0], 1, l):
            ret += s
print(ret)

        