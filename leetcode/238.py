class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pf = [1] * (n+1)
        for i in range(n):
            x = nums[i]
            pf[i+1] = pf[i] * x
        sf = [1] * (n+1)
        for i in range(n-1, -1, -1):
            x = nums[i]
            sf[i] = sf[i+1] * x
        ret = []
        for i in range(n):
            ret.append(pf[i] * sf[i+1])
        return ret