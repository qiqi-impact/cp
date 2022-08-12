class Solution:
    def solve(self, nums):
        if not nums: return False
        mxa = [nums[0]]
        for i in range(1, len(nums)):
            mxa.append(max(mxa[-1], nums[i]))
        mn = nums[-1]
        for i in range(len(nums)-1, 0, -1):
            mn = min(mn, nums[i])
            if mn > mxa[i-1]:
                return True
        return False