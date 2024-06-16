class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        power.sort()
        @cache
        def dp(idx, lst):
            if idx == len(power):
                return 0
            v = power[idx]
            ret = dp(idx+1, max(lst, v - 3))
            if v - lst not in [1, 2]:
                ret = max(ret, v + dp(idx+1, v))
            return ret
        return dp(0, -inf)