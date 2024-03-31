class Solution:
    def maxBottlesDrunk(self, b: int, e: int) -> int:
        ret = 0
        cur = b
        while cur >= e:
            ret += e
            cur = cur - e + 1
            e += 1
        return ret + cur