class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ret = 0
        for x in nums:
            if x%3 != 0:
                ret += 1
        return ret