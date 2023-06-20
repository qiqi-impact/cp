class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        if (len(stones)-1) % (k-1) != 0:
            return -1

        pf = [0]
        for x in stones:
            pf.append(pf[-1] + x)

        @cache
        def dp(l, r):
            if l == r:
                return 0
            path = []
            ret = inf
            def f(idx, cl, cost):
                nonlocal ret, path
                if idx == k:
                    ret = min(ret, cost + sum(path))
                    return
                if idx == k-1:
                    mr = r
                else:
                    mr = cl
                for cr in range(mr, r+1-(k-1-idx), k-1):
                    q = dp(cl, cr)
                    rem = pf[cr+1] - pf[cl]
                    path.append(rem)
                    f(idx+1, cr+1, cost+q)
                    path.pop()
            f(0, l, 0)
            return ret
        return dp(0, len(stones)-1)

