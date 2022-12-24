class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        pf = [0]
        for x in nums:
            pf.append(pf[-1] + x)
            
        ret = -1
        stack = []
        for i, x in enumerate(nums):
            idx = i
            while stack and stack[-1][1] >= x:
                a, b = stack.pop()
                ret = max(ret, (pf[i] - pf[a]) * b)
                idx = a
            stack.append([idx, x])
            
        for a, b in stack:
            ret = max(ret, (pf[-1] - pf[a]) * b)
        
        return ret % (10**9+7)