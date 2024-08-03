class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        ret = 0
        for i in range(R//2):
            for j in range(C//2):
                ci, cj = R-1-i, C-1-j
                a, b, c, d = grid[i][j], grid[ci][j], grid[i][cj], grid[ci][cj]
                t = a+b+c+d
                ret += min(t, 4-t)
                
        cur = 0
        tot = 0
        if R % 2:
            for j in range(C//2):
                cur += (grid[R//2][j] != grid[R//2][C-1-j])
            for j in range(C):
                tot += grid[R//2][j]
                
        if C % 2:
            for i in range(R//2):
                cur += (grid[i][C//2] != grid[R-1-i][C//2])
            for i in range(R):
                tot += grid[i][C//2]
                
        if R %2 and C % 2:
            tot -= 2 * grid[R//2][C//2]
            
        ret += cur
        tot %= 4
        if tot and cur == 0:
            ret += 2
        
        if R % 2 and C % 2:
            ret += grid[R//2][C//2]
        
        return ret
        