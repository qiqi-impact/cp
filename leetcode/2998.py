class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        @cache
        def dp(t):
            if t <= y:
                return y - t
            ret = t - y
            for q in [5, 11]:
                m = t%q
                ret = min(ret, 1+m+dp(t//q))
                ret = min(ret, 1+q-m+dp(t//q+1))
            return ret
        return dp(x)