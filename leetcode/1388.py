class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        @cache
        def dp(l, r, k):
            if k == 0:
                return 0
            if l > r:
                return float('-inf')
            ret = slices[l] + dp(l+2, r - int(l == 0), k-1)
            ret = max(ret, dp(l+1, r, k))
            return ret
        return dp(0, len(slices)-1, len(slices)//3)