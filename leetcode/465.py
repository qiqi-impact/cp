class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        @cache
        def f(*t):
            tt = list(t)
            if len(tt) == 0:
                return 0
            ret = float('inf')
            for i in range(len(tt)-1):
                if tt[i] > 0:
                    break
                amt = min(-tt[i], tt[-1])
                tt[i] += amt
                tt[-1] -= amt
                ret = min(ret, 1 + f(*tuple(sorted([x for x in tt if x != 0]))))
                tt[i] -= amt
                tt[-1] += amt
            return ret
        d = defaultdict(int)
        for x, y, z in transactions:
            d[x] -= z
            d[y] += z
            
        return f(*sorted([x for x in list(d.values()) if x != 0]))