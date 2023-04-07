class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        w = 2 * k + 1
        ret = [-1] * len(nums)
        if w > len(nums):
            return ret
        cur = 0
        for i in range(w):
            cur += nums[i]
        ret[k] = cur // w
        for i in range(w, len(nums)):
            cur += nums[i] - nums[i-w]
            ret[i-k] = cur // w
        return ret