class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        mx, cur = 0, 0
        for i in range(len(nums)):
            cur += nums[i] 
            mx = max(mx, ceil(cur / (i+1)))
        return mx