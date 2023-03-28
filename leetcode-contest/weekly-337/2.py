class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        l = [None] * (n*n)
        for i in range(n):
            for j in range(n):
                l[grid[i][j]] = (i, j)
                
        if l[0] != (0, 0):
            return False
                
        cur = None
        for x, y in l:
            if cur == None:
                cur = (x, y)
            else:
                dx = abs(cur[0] - x)
                dy = abs(cur[1] - y)
                if not ((dx == 2 and dy == 1) or (dx == 1 and dy == 2)):
                    return False
                cur = (x, y)
        return True