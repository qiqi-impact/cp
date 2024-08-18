class Solution:
    def maxEnergyBoost(self, a: List[int], b: List[int]) -> int:
        n = len(a)
        @cache
        def dp(idx, lst):
            if idx >= n:
                return 0
            if lst == 0:
                ret = a[idx] + dp(idx + 1, 0)
                ret = max(ret, dp(idx + 1, 1))
            else:
                ret = b[idx] + dp(idx + 1, 1)
                ret = max(ret, dp(idx + 1, 0))
            return ret
        return max(dp(0, 0), dp(0, 1))            
            