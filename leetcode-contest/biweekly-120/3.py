class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        l = []
        r = []
        n = len(nums)
        cur = -inf
        for i in range(n):
            if nums[i] > cur:
                l.append(nums[i])
            else:
                break
            cur = nums[i]
            
        cur = inf
        for i in range(n-1, -1, -1):
            if nums[i] < cur:
                r.append(nums[i])
            else:
                break
            cur = nums[i]
        r = r[::-1]
        
        if len(l) == n:
            return n * (n+1) // 2
        
        ret = len(r)+1
        for x in l:
            idx = bisect.bisect_left(r, x+1)
            ret += len(r) - idx + 1
        return ret
            