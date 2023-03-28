class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        l = []
        for i in range(R):
            for j in range(C):
                l.append((matrix[i][j], i, j))
        l.sort()
        
        @cache
        def dfs(i, j):
            ret = 0
            for dx, dy in pairwise([1, 0, -1, 0, 1]):
                nx, ny = i+dx, j+dy
                if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny] > matrix[i][j]:
                    ret = max(ret, dfs(nx, ny))
            return ret + 1
        
        ans = 0
        for _, i, j in l:
            ans = max(ans, dfs(i, j))
        return ans