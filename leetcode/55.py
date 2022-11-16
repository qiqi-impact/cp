class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        for i in range(len(nums)):
            if i > mx:
                return False
            if i == len(nums)-1:
                return True
            mx = max(mx, nums[i] + i)