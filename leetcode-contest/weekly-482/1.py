class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        pf = [0]
        for i in range(len(nums)):
            pf.append(pf[-1] + nums[i])
        ret = -inf
        mn = inf
        for i in range(len(nums)-1, 0, -1):
            mn = min(mn, nums[i])
            ret = max(ret, pf[i] - mn)
        return ret