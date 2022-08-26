class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l,r = None, None
            
        def find_best(l, r):
            if l == r:
                return nums[l]
            fn, ln, nct = None, None, 0
            for i in range(l, r+1):
                if nums[i] < 0:
                    nct += 1
                    if fn is None:
                        fn = i
                    ln = i
            if nct % 2 == 0:
                return math.prod(nums[l:r+1])
            q = -1e18
            if ln > l:
                q = max(q, math.prod(nums[l:ln]))
            if fn < r:
                q = max(q, math.prod(nums[fn+1:r+1]))
            return q
        
        ret = math.prod(nums)
        
        for i in range(len(nums)):
            if nums[i] != 0:
                if l is None:
                    l = i
                r = i
            elif l is not None:
                ret = max(ret, find_best(l, r))
                l, r = None, None
        if l is not None:
            ret = max(ret, find_best(l, r))
        return ret
                