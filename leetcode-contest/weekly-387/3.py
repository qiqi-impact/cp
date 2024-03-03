class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def f(a, b):
            r = 0
            for i in range(n):
                for j in range(n):
                    if i >= n//2:
                        sh = j == n//2
                    else:
                        sh = (i == j) or (i == n-1-j)
                    if (sh and grid[i][j] != a) or ((not sh) and grid[i][j] != b):
                        r += 1
            return r
        
        ret = inf
        for x in range(3):
            for y in range(3):
                if x != y:
                    ret = min(ret, f(x, y))
        return ret