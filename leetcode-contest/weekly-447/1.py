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
            xi = bisect.bisect_left(xc[x], y)
            yi = bisect.bisect_left(yc[y], x)
            if 1 <= xi < len(xc[x]) - 1 and 1 <= yi < len(yc[y]) - 1:
                ret += 1
            
        return ret