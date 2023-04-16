class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        ret = None
        mx = -1
        for d in sorted(divisors):
            ct = 0
            for x in nums:
                if x%d == 0:
                    ct += 1
            if ct > mx:
                mx = ct
                ret = d
        return ret