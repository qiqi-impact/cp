class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ret = 0
        mx = 0
        for x, y in dimensions:
            t = x*x + y*y
            if t > mx:
                mx = t
                ret = x*y
            elif t == mx:
                ret = max(ret, x*y)
        return ret