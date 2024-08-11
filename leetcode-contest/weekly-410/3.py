class Solution:
    def countOfPairs(self, a: List[int]) -> int:
        n = len(a)
        MOD = 10**9+7
        @cache
        def dp(idx, lst):
            if idx == n:
                return 1
            olst = inf if idx == 0 else a[idx-1] - lst
            ret = 0
            for i in range(lst, 51):
                if i <= a[idx] and a[idx] - i <= olst:
                    ret += dp(idx+1, i)
                    ret %= MOD
            return ret
        return dp(0, 0)