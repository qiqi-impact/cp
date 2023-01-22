class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        ret = inf
        for i in range(len(nums)+1):
            l, r = inf, -inf
            if i > 0:
                l = min(l, nums[0] + k)
                r = max(r, nums[i-1] + k)
            if i < len(nums):
                l = min(l, nums[i] - k)
                r = max(r, nums[-1] - k)
            ret = min(ret, r - l)
        return ret