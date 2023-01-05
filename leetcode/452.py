class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        last = float('-inf')
        ret = 0
        points.sort(key=lambda x:x[1])
        for x, y in points:
            if last < x:
                last = y
                ret += 1
        return ret