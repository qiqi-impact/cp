class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        ct = [set() for _ in range(101)]
        mx = 0
        for i in range(R):
            for j in range(C):
                ct[grid[i][j]].add(i)
                mx = max(mx, grid[i][j])
        
        @cache
        def dp(idx, b):
            if idx == mx+1:
                return 0
            ret = dp(idx+1, b)
            for x in ct[idx]:
                if not b & 1 << x:
                    ret = max(ret, dp(idx+1, b | 1 << x) + idx)
            return ret
        return dp(1, 0)