class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        mx = max(len(r) for r in grid)
        ret = [0] * mx
        for r in grid:
            for i in range(len(r)):
                ret[i] = max(ret[i], len(str(r[i])))
        return ret