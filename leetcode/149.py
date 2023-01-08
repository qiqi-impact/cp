class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        xct = defaultdict(int)
        for x, _ in points:
            xct[x] += 1
        ret = max(xct.values())
        
        if len(points) <= 2:
            return len(points)
        
        for i in range(len(points)):
            x0, y0 = points[i]
            slp = defaultdict(int)
            for j in range(i+1, len(points)):
                x1, y1 = points[j]
                if x1 == x0:
                    continue
                a, b = x1 - x0, y1 - y0
                slp[b/a] += 1
                ret = max(ret, 1+max(slp.values()))
        return ret