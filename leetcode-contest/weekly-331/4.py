class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        ct = defaultdict(int)
        a, b = defaultdict(int), defaultdict(int)
        for x in basket1:
            ct[x] += 1
            a[x] += 1
        for x in basket2:
            ct[x] += 1
            b[x] += 1
        for k in ct:
            if ct[k] % 2:
                return -1
        l, r = [], []
        for k in ct:
            df = ct[k]//2 - a[k]
            if df > 0:
                r += [k] * df
            else:
                l += [k] * (-df)
        
        l.sort()
        r.sort()
        ret = 0
        alt = min(basket1 + basket2) * 2
        for i in range(len(l)):
            ret += min(l[i], r[len(r)-1-i], alt)
        return ret