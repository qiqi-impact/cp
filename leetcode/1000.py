class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        if (len(stones)-1) % (k-1) != 0:
            return -1

        pf = [0]
        for x in stones:
            pf.append(pf[-1] + x)

        @cache
        def dp(l, r, p):
            if l >= r:
                return 0
            ret = inf
            if p == 1:
                mr = r
            else:
                mr = l
            for cr in range(mr, r+1-(p-1), k-1):
                q = dp(l, cr, k)
                ret = min(ret, q + dp(cr+1, r, p-1))
            if p == k:
                ret += pf[r+1] - pf[l]
            return ret
        return dp(0, len(stones)-1, k)
