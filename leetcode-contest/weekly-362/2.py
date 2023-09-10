class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dx = abs(sx - fx)
        dy = abs(sy - fy)
        if t == 1 and max(dx, dy) == 0:
            return False
        return max(dx, dy) <= t