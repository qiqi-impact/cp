class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        usageLimits.sort()
        cur = 0
        ret = 0
        for x in usageLimits:
            cur += x
            if (ret + 1) * (ret + 2) // 2 <= cur:
                ret += 1
        return ret