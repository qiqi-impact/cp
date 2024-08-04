class neighborSum:

    def __init__(self, grid: List[List[int]]):
        R, C = len(grid), len(grid[0])
        self.g = grid
        self.d = {}
        for i in range(R):
            for j in range(C):
                self.d[grid[i][j]] = (i, j)
                
            

    def adjacentSum(self, value: int) -> int:
        R, C = len(self.g), len(self.g[0])
        i, j = self.d[value]
        ret = 0
        for (dx, dy) in [[-1,0],[1,0],[0,1],[0,-1]]:
            nx, ny = i + dx, j + dy
            if 0 <= nx < R and 0 <= ny < C:
                ret += self.g[nx][ny]
        return ret

    def diagonalSum(self, value: int) -> int:
        R, C = len(self.g), len(self.g[0])
        i, j = self.d[value]
        ret = 0
        for (dx, dy) in [[-1,-1],[1,1],[-1,1],[1,-1]]:
            nx, ny = i + dx, j + dy
            if 0 <= nx < R and 0 <= ny < C:
                ret += self.g[nx][ny]
        return ret
        


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)