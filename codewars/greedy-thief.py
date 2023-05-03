from preloaded import Item
from functools import cache
import math

def greedy_thief( items:list[Item], n:int) -> list[Item] :
    @cache
    def dfs(idx, left):
        if idx == len(items):
            return 0, None
        la, lb = dfs(idx+1, left)
        ra, rb = -math.inf, -math.inf
        a, b = items[idx]
        if a <= left:
            ra, rb = dfs(idx+1, left - a)
            ra += b
        if la >= ra:
            return la, 0
        else:
            return ra, 1
    path = []
    for i in range(len(items)):
        a, b = dfs(i, n)
        if b == 1:
            n -= items[i][0]
            path.append(items[i])
    return path