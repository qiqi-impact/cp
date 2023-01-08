class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        p, n = 0, 0
        for x in nums:
            if x < 0:
                n += 1
            elif x > 0:
                p += 1
        return max(n, p)