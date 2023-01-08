class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        ret = 0
        for i in range(len(points)):
            x0, y0 = points[i]
            for j in range(i+1, len(points)):
                x1, y1 = points[j]
                cur = 2
                for k in range(j+1, len(points)):
                    x2, y2 = points[k]
                    if (x2 - x0) * (y1 - y0) == (x1 - x0) * (y2 - y0):
                        cur += 1
                ret = max(ret, cur)
        return ret