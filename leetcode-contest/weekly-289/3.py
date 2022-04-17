class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        
        prod = [[[] for i in range(c)] for j in range(r)]
        for i in range(r):
            for j in range(c):
                prod[i][j] = [0,0]
                for p, k in enumerate([2,5]):
                    while grid[i][j] % k == 0:
                        grid[i][j] //= k
                        prod[i][j][p] += 1
        left = [[None for i in range(c+1)] for j in range(r)]
        up = [[None for i in range(c)] for j in range(r+1)]
        for i in range(r):
            for j in range(c+1):
                left[i][j] = [0,0]
                if j > 0:
                    for k in [0, 1]:
                        left[i][j][k] = left[i][j-1][k] + prod[i][j-1][k]
        for j in range(c):
            for i in range(r+1):
                up[i][j] = [0,0]
                if i > 0:
                    for k in [0, 1]:
                        up[i][j][k] = up[i-1][j][k] + prod[i-1][j][k]
        
        if r == 1:
            return min(left[0][c][0], left[0][c][1])
        if c == 1:
            return min(up[r][0][0], up[r][0][1])
        
                
        ret = 0
        
        for i in range(r):
            for j in range(c):
                a0 = left[i][j][0] - left[i][0][0]
                a1 = left[i][j][1] - left[i][0][1]
                if j < c-1:
                    b0 = left[i][c][0] - left[i][j+1][0]
                    b1 = left[i][c][1] - left[i][j+1][1]
                
                c0 = up[i][j][0] - up[0][j][0]
                c1 = up[i][j][1] - up[0][j][1]
                if i < r-1:
                    d0 = up[r][j][0] - up[i+1][j][0]
                    d1 = up[r][j][1] - up[i+1][j][1]
                
                h = []
                if j > 0:
                    h.append([a0,a1])
                if j < c-1:
                    h.append([b0,b1])
                    
                v = []
                if i > 0:
                    v.append([c0,c1])
                if i < r-1:
                    v.append([d0,d1])
                    
                for [a,b] in h:
                    for [q, d] in v:
                        ret = max(ret, min(prod[i][j][0]+a+q, prod[i][j][1]+b+d))
                        # print(min(a+q, b+d))
                        
        return ret
        