class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        R, C = len(grid), len(grid[0])
        ct = [0] * (R * R+1)
        for i in range(R):
            for j in range(R):
                ct[grid[i][j]] += 1
        ret = [None, None]
        for i in range(1, R*R+1):
            if ct[i] == 2:
                ret[0] = i
            elif ct[i] == 0:
                ret[1] = i
        return ret