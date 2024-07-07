class Solution:
    def numberOfSubmatrices(self, g: List[List[str]]) -> int:
        R, C = len(g), len(g[0])
        x, y = [[0 for _ in range(C)] for _ in range(R)], [[0 for _ in range(C)] for _ in range(R)]
        ret = 0
        for i in range(R):
            for j in range(C):
                if i > 0:
                    x[i][j] += x[i-1][j]
                    y[i][j] += y[i-1][j]
                if j > 0:
                    x[i][j] += x[i][j-1]
                    y[i][j] += y[i][j-1]
                if i > 0 and j > 0:
                    x[i][j] -= x[i-1][j-1]
                    y[i][j] -= y[i-1][j-1]
                x[i][j] += int(g[i][j] == 'X')
                y[i][j] += int(g[i][j] == 'Y')
                if x[i][j] > 0 and x[i][j] == y[i][j]:
                    ret += 1
        return ret