class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        ct = [0] * C
        ret = 0
        for i in range(R):
            for j in range(C):
                if matrix[i][j]:
                    ct[j] += 1
                else:
                    ct[j] = 0
            sct = sorted(ct, reverse=True)
            for k in range(C):
                ret = max(ret, (k+1) * sct[k])
        return ret