class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        n = len(nums)
        b = list(range(1, n)) + [n-1]
        nums.sort()
        return nums == b