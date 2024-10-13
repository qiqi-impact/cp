class Solution:
    def countWinningSequences(self, s: str) -> int:
        d = {'F':0, 'W':1, 'E':2}
        ev = [[0,-1,1], [1,0,-1], [-1,1,0]]
        s = [d[x] for x in s]
        @cache
        def dp(idx, score, lst):
            if idx == len(s):
                return int(score > 0)
            v = s[idx]
            ret = 0
            for i in range(3):
                if i != lst:
                    ns = score + ev[i][v]
                    ret += dp(idx + 1, ns, i)
            return ret % (10**9+7)
        r = dp(0, 0, -1)
        dp.cache_clear()
        return r