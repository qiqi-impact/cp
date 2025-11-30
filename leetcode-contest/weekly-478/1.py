class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        ct = 0
        for i in range(len(nums) - 1, -1, -1):
            if i < len(nums) - 1 and nums[i] < nums[i+1]:
                ct = len(nums) - 1 - i
            if ct >= k:
                return i + 1
        return 0