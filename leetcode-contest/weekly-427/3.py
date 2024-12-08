class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        d[k-1] = 0
        cur = 0
        ret = -inf
        for i, x in enumerate(nums):
            cur += x
            ret = max(ret, cur - d.get(i%k, inf))
            d[i%k] = min(d.get(i%k, inf), cur)
        return ret