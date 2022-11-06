class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        sm = 0
        for i in range(k):
            n = nums[i]
            d[n] = d.get(n, 0) + 1
            sm += n
        ret = 0
        if len(d) == k:
            ret = max(ret, sm)
        for i in range(k, len(nums)):
            d[nums[i-k]] -= 1
            sm -= nums[i-k]
            if d[nums[i-k]] == 0:
                del d[nums[i-k]]
            n = nums[i]
            d[n] = d.get(n, 0) + 1
            sm += n
            if len(d) == k:
                ret = max(ret, sm)
        return ret