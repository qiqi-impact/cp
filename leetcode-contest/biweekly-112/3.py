class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        ct = {}
        ret = 0
        sm = 0
        for i in range(k):
            v = nums[i]
            if v not in ct:
                ct[v] = 0
            ct[v] += 1
            sm += v
        if len(ct) >= m:
            ret = sm
        for i in range(k, len(nums)):
            ct[nums[i]] = ct.get(nums[i], 0) + 1
            ct[nums[i-k]] -= 1
            
            if not ct[nums[i-k]]:
                del ct[nums[i-k]]
            
            sm += nums[i]
            sm -= nums[i-k]
            if len(ct) >= m:
                ret = max(ret, sm)
        return ret