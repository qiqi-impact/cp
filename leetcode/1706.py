class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        R, C = len(grid), len(grid[0])
        ret = [-1] * C
        for j in range(C):
            cur = j
            for i in range(R+1):
                if i == R:
                    ret[j] = cur
                elif grid[i][cur] == 1:
                    if cur == C-1 or grid[i][cur+1] == -1:
                        break
                    cur += 1
                else:
                    if cur == 0 or grid[i][cur-1] == 1:
                        break
                    cur -= 1
        return ret