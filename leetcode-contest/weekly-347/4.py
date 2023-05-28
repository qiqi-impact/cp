class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        R, C = len(mat), len(mat[0])
        d = defaultdict(list)
        ans = [[0 for _ in range(C)] for _ in range(R)]
        for i in range(R):
            for j in range(C):
                d[mat[i][j]].append((i, j))
        mr = [0] * R
        mc = [0] * C
        for k in sorted(d.keys(), reverse=True):
            for (i, j) in d[k]:
                ans[i][j] = max(mr[i], mc[j])+1
            for (i, j) in d[k]:
                mr[i] = max(mr[i], ans[i][j])
                mc[j] = max(mc[j], ans[i][j])
        return max(max(mr), max(mc))
    