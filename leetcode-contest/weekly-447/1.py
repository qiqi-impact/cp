class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        xc = defaultdict(list)
        yc = defaultdict(list)

        for x, y in buildings:
            xc[x].append(y)
            yc[y].append(x)

        for k in xc:
            xc[k].sort()

        for k in yc:
            yc[k].sort()
        
        ret = 0
        for x, y in buildings:
            if xc[x][0] != y and xc[x][-1] != y and yc[y][0] != x and yc[y][-1] != x:
                ret += 1
            
        return ret