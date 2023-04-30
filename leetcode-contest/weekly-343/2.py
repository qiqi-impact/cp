class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        R, C = len(mat), len(mat[0])
        r = [0] * R
        c = [0] * C
        
        inv = {}
        for i in range(R):
            for j in range(C):
                inv[mat[i][j]] = (i, j)
        
        for i, e in enumerate(arr):
            x, y = inv[e]
            r[x] += 1
            c[y] += 1
            if r[x] == C or c[y] == R:
                return i