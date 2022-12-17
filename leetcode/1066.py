class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        W = len(workers)
        FULL = (1 << W) - 1
        
        @cache
        def dp(idx, b):
            if b == FULL:
                return 0
            if idx == len(bikes):
                return 1e9
            ret = dp(idx+1, b)
            for i in range(W):
                if not (1 & (b >> i)):
                    ret = min(ret, abs(bikes[idx][0] - workers[i][0]) + abs(bikes[idx][1] - workers[i][1]) + dp(idx+1, b ^ (1 << i)))
            return ret
        
        return dp(0, 0)