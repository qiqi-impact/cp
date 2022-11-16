class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        ret = [[None for _ in range(C)] for _ in range(R)]
        l = []
        for i in range(R):
            for j in range(C):
                l.append((grid[i][j], i, j))
        l.sort()
        mxr = [0 for _ in range(R)]
        mxc = [0 for _ in range(C)]
        for _, i, j in l:
            v = 1 + max(mxr[i], mxc[j])
            mxr[i] = v
            mxc[j] = v
            ret[i][j] = v
        return ret