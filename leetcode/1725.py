class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        mx = 0
        for x, y in rectangles:
            mx = max(mx, min(x,y))
        ret = 0
        for x, y in rectangles:
            ret += min(x,y)==mx
        return ret