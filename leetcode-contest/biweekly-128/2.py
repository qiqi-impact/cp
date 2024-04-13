class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        s = set()
        for x, y in points:
            s.add(x)
        l = sorted(s)
        ret = 0
        lst = -inf
        for x in l:
            if x - lst > w:
                lst = x
                ret += 1
        return ret