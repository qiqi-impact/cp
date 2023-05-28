class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        ret = [[None for _ in range(C)] for _ in range(R)]
        for i in range(R):
            for j in range(C):
                a = set()
                cx, cy = i-1, j-1
                while 0 <= cx < R and 0 <= cy < C:
                    a.add(grid[cx][cy])
                    cx -= 1
                    cy -= 1
                la = len(a)
                
                a = set()
                cx, cy = i+1, j+1
                while 0 <= cx < R and 0 <= cy < C:
                    a.add(grid[cx][cy])
                    cx += 1
                    cy += 1
                lb = len(a)
                ret[i][j] = abs(lb - la)
        return ret
                