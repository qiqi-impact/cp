class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        R = len(grid)
        ret = [[None for _ in range(R-2)] for _ in range(R-2)]
        for i in range(R-2):
            for j in range(R-2):
                mx = float('-inf')
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        mx = max(mx, grid[i+1+dx][j+1+dy])
                ret[i][j] = mx
        return ret