class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        cur = -inf
        ret = 0
        for x in nums:
            if x >= cur:
                cur = x
                ret += 1
        return ret