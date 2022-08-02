class Solution:
    def solve(self, matrix):
        R, C = len(matrix), len(matrix[0])
        @cache
        def dfs(i, j, lm):
            nonlocal mx
            ret = 1
            if lm != 'l' and j+1 < C and matrix[i][j+1] == 0:
                ret = max(ret, 1 + dfs(i, j+1, 'r'))
            if lm != 'r' and j-1 >= 0 and matrix[i][j-1] == 0:
                ret = max(ret, 1 + dfs(i, j-1, 'l'))
            if i != R-1 and matrix[i+1][j] == 0:
                ret = max(ret, 1 + dfs(i+1, j, 'd'))
            if i != R-1 and ret == 1:
                return float('-inf')
            return ret
        l = [0] + [dfs(0, j, 'd') for j in range(C) if matrix[0][j] == 0]
        return max(l)