class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        cur = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                cur += nums[i]
            else:
                break
        s = set(nums)
        for j in range(cur, 10**9):
            if j not in s:
                return j