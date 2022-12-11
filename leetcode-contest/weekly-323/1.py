class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            grid[i].sort()
        ret = 0
        for j in range(len(grid[0])):
            m = 0
            for i in range(len(grid)):
                m = max(m, grid[i][j])
            ret += m
        return ret