class Solution:
    def minOperations(self, nums: List[int]) -> int:
        f = 0
        for i in range(len(nums)):
            if (nums[i] + f)%2 == 0:
                f += 1
        return f