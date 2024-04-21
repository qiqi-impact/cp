class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        ct = [[0]*10 for _ in range(C)]
        for i in range(R):
            for j in range(C):
                ct[j][grid[i][j]] += 1
                
        @cache
        def dp(j, lst):
            if j == C:
                return 0
            ret = inf
            for x in range(10):
                if x != lst:
                    ret = min(ret, R - ct[j][x] + dp(j+1, x))
            return ret
        
        return dp(0, -1)