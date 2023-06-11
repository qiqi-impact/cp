class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        if len(nums) == 1:
            return nums[0]
        ret = sum(nums)
        cc = 0
        for _ in range(len(nums)):
            cc += x
            tt = nums[:]
            for i in range(len(nums)):
                tt[i] = min(nums[i], nums[(i+1)%len(nums)])
            nums = tt
            ret = min(ret, cc + sum(nums))
        return ret