class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ret = 0
        sm = 0
        for i in range(len(nums)):
            sm += nums[i]
            ret = max(ret, math.ceil(sm/(i+1)))
        return ret