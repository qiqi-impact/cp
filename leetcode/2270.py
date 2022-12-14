class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        sm = sum(nums)
        cur = 0
        ret = 0
        for i in range(len(nums)-1):
            cur += nums[i]
            if cur >= sm - cur:
                ret += 1
        return ret