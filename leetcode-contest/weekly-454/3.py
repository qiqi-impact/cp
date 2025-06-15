class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        n = len(nums)
        ret = -inf
        best = [inf, -inf]
        for i in range(n):
            if i >= m - 1:
                best[0] = min(best[0], nums[i - (m - 1)])
                best[1] = max(best[1], nums[i - (m - 1)])
            v = nums[i]
            if best[0] != inf:
                ret = max(ret, v*best[0])
            if best[1] != -inf:
                ret = max(ret, v*best[1])
            
        return ret