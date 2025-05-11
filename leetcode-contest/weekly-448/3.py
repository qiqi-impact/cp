def addmult(amt, loop, start):
    if amt == 1:
        return 0
    ret = 0
    cur = start
    for i in range((amt - 1) // 2):
        ret += cur * (cur + 2)
        cur += 2
    # print(ret, amt, cur, start)
    cur = start + 1
    for i in range((amt - 2) // 2):
        ret += cur * (cur + 2)
        cur += 2
    # print(ret)
    ret += (start + amt - 1) * (start + amt - 2)
    if loop:
        ret += start * (start + 1)
    # print(amt, loop, start, ret)
    return ret

class Solution:
    def maxScore(self, n: int, edges: List[List[int]]) -> int:
        cc = [None] * n
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        ct = 0
        hasleaf = []
        sz = []
        def dfs(idx):
            nonlocal ct
            if len(g[idx]) == 1:
                hasleaf[ct] = 1
            sz[ct] += 1
            for o in g[idx]:
                if cc[o] is None:
                    cc[o] = ct
                    dfs(o)
        for i in range(n):
            if cc[i] is None:
                hasleaf.append(0)
                sz.append(0)
                cc[i] = ct
                dfs(i)
                ct += 1
        q = sorted(list(zip(hasleaf, sz)), key=lambda x:(x[1] != 1, -x[0], x[1]))
        st = 1
        ret = 0
        # print(q)
        for b, s in q:
            ret += addmult(s, not b, st)
            st += s
        return ret