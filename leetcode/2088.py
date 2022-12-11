class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        ret = 0
        def process(g):
            ret = 0
            left = [[0 for _ in range(C)] for _ in range(R)]
            right = [[0 for _ in range(C)] for _ in range(R)]
            for i in range(R):
                for j in range(C):
                    if g[i][j]:
                        other = 0
                        if i > 0 and j > 0:
                            other = min(left[i-1][j], left[i][j-1])
                        left[i][j] = 1 + other
            for i in range(R):
                for j in range(C-1, -1, -1):
                    if g[i][j]:
                        other = 0
                        if i > 0 and j < C-1:
                            other = min(right[i-1][j], right[i][j+1])
                        right[i][j] = 1 + other
            pyr = [[0 for _ in range(C)] for _ in range(R)]
            for i in range(R):
                for j in range(C):
                    pyr[i][j] = max(0, min(left[i][j], right[i][j]) - 1)
                    ret += pyr[i][j]
            return ret
               
        return process(grid) + process(grid[::-1])