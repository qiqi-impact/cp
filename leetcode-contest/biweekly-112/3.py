class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        ct = {}
        ret = 0
        sm = 0
        for i in range(len(nums)):
            ct[nums[i]] = ct.get(nums[i], 0) + 1
            sm += nums[i]
            if i >= k:
                ct[nums[i-k]] -= 1
                if not ct[nums[i-k]]:
                    del ct[nums[i-k]]
                sm -= nums[i-k]
            if len(ct) >= m and i >= k-1:
                ret = max(ret, sm)
        return ret