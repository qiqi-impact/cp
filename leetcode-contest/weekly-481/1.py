class Solution:
    def mirrorDistance(self, n: int) -> int:
        s = int(str(n)[::-1])
        return abs(s - n)