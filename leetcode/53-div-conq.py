class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = max(nums)
        if mx < 0:
            return mx
        ans = -inf
        def dfs(l, r):
            nonlocal ans
            if l == r:
                ans = max(ans, nums[l])
                return [nums[l], nums[l], nums[l]]
            ret = [0, 0, 0]
            mi = (l+r)//2
            a, b, c = dfs(l, mi)
            d, e, f = dfs(mi+1, r)
            ans = max(ans, b+d)
            ret[0] = max(ret[0], a, c+d)
            ret[1] = max(ret[1], e, f+b)
            ret[2] = c+f
            return ret
        dfs(0, len(nums)-1)
        return ans