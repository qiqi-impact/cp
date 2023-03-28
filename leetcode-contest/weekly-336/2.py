class Solution:
    def maxScore(self, nums: List[int]) -> int:
        ret = 0
        nums.sort(reverse=True)
        cur = 0
        for x in nums:
            cur += x
            if cur > 0:
                ret += 1
        return ret