class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        def to_int(i, j):
            return i*C+j
        
        def to_coord(t):
            return (t//C, t%C)
        
        ALLVIS = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    sx, sy = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                if grid[i][j] != -1:
                    ALLVIS ^= (1 << to_int(i, j))
        
        @cache
        def dp(i, j, vis):
            if (i, j) == end:
                return int(vis == ALLVIS)
            ret = 0
            for dx, dy in pairwise([1,0,-1,0,1]):
                nx, ny = i+dx, j+dy
                if 0 <= nx < R and 0 <= ny < C and not vis & (1 << to_int(nx, ny)):
                    ret += dp(nx, ny, vis ^ (1 << to_int(nx, ny)))
            return ret
        
        return dp(sx, sy, 1 << to_int(sx, sy))