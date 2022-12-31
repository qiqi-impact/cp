class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        for i in range(len(nums)):
            if i > mx:
                return False
            mx = max(mx, nums[i] + i)
            if mx >= len(nums)-1:
                return True