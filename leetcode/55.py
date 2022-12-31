class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0 # mx = "how far can I go given the previous jump lengths"
        for i in range(len(nums)):
            if i > mx:
                return False
            mx = max(mx, nums[i] + i)
            if mx >= len(nums)-1:
                return True