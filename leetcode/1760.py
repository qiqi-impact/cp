class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        nums.sort(reverse=True)
        
        def can(x):
            ret = 0
            for n in nums:
                if n <= x:
                    return True
                ret += max(0, (n + x - 1) // x - 1)
                if ret > maxOperations:
                    return False
            return True
            
        l, r = 1, max(nums)
        while l < r:
            mi = (l+r)//2
            if can(mi):
                r = mi
            else:
                l = mi + 1
        return r