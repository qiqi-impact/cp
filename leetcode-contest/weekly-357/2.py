class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        if len(nums) <= 2: return True
        for x, y in pairwise(nums):
            if x+y >= m:
                return True
        return False