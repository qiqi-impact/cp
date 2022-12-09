class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        R, C = len(grid), len(grid[0])
        empty = [[0 for _ in range(C+1)] for _ in range(R+1)]
        stamp = [[0 for _ in range(C+1)] for _ in range(R+1)]
        for i in range(R-1, -1, -1):
            for j in range(C-1, -1, -1):
                empty[i][j] = 1 - grid[i][j] + empty[i+1][j] + empty[i][j+1] - empty[i+1][j+1]
        for i in range(R-stampHeight+1):
            for j in range(C-stampWidth+1):
                if empty[i][j] - empty[i+stampHeight][j] - empty[i][j+stampWidth] + empty[i+stampHeight][j+stampWidth] == stampHeight * stampWidth:
                    stamp[i][j] += 1
                    stamp[i+stampHeight][j] -= 1
                    stamp[i][j+stampWidth] -= 1
                    stamp[i+stampHeight][j+stampWidth] += 1
        for i in range(R):
            for j in range(C):
                empty[i][j] = stamp[i][j] + empty[i-1][j] + empty[i][j-1] - empty[i-1][j-1]
                if empty[i][j] == 0 and grid[i][j] == 0:
                    return False
        return True