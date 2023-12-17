class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        def can(x):
            if x == 1:
                return True
            s = 0
            for i in range(x//2):
                s -= nums[i]
            for i in range(x//2, x):
                s += nums[i]
            ret = s + nums[x//2] * ((x//2) - (x - (x//2)))
            for j in range(x, len(nums)):
                s += nums[j] + nums[j-x] - 2 * nums[j-x+x//2]
                ret = min(ret, s + nums[x//2+j-x+1] * ((x//2) - (x - (x//2))))
            return ret <= k
        
        l, r = 1, len(nums)
        while l < r:
            mi = (l+r+1)//2
            if can(mi):
                l = mi
            else:
                r = mi - 1
        return l