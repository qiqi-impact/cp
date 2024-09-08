class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        ret = 0
        mx = 0
        for i in range(len(nums)-1):
            v = nums[i]
            mx = max(mx, v)
            ret += mx
        return ret