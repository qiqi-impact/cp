class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        xc = {}
        yc = {}

        for x, y in buildings:
            if x not in xc:
                xc[x] = [y, y]
            if y not in yc:
                yc[y] = [x, x]
            xc[x][0] = min(xc[x][0], y)
            xc[x][1] = max(xc[x][1], y)
            yc[y][0] = min(yc[y][0], x)
            yc[y][1] = max(yc[y][1], x)
        
        ret = 0
        for x, y in buildings:
            if xc[x][0] != y and xc[x][-1] != y and yc[y][0] != x and yc[y][-1] != x:
                ret += 1
            
        return ret