class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        pf = [0]
        for x in nums:
            pf.append(pf[-1] + x)
        
        @cache
        def valid(l, r):
            return l == r or pf[r+1] - pf[l] >= m
        
        @cache
        def can(l, r):
            if l == r:
                return True
            for i in range(l, r):
                if valid(l, i) and valid(i+1, r) and can(l, i) and can(i+1, r):
                    return True
            return False
        
        return can(0, len(nums)-1)