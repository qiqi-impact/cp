class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = 10**9+7
        @cache
        def dp(x, idx):
            if x == 0:
                return 1
            if idx == len(types):
                return 0
            ret = dp(x, idx+1)
            for t in range(types[idx][0]):
                x -= types[idx][1]
                if x < 0:
                    break
                ret += dp(x, idx+1)
                ret %= MOD
            return ret
        return dp(target, 0)