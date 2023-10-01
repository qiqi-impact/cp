class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        mxr = [-inf] * n
        for i in range(n-2, -1, -1):
            mxr[i] = max(mxr[i+1], nums[i+1])
        mx = -inf
        mxd = -inf
        ret = 0
        for i in range(len(nums)):
            c = nums[i]
            mxd = max(mxd, mx - c)
            mx = max(mx, c)
            if mxd > 0:
                ret = max(ret, mxd * mxr[i])
        return ret