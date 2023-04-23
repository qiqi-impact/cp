class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        ct = 0
        for x in nums:
            if x == 1:
                ct += 1
        if ct:
            return len(nums) - ct
        
        for l in range(2, n+1):
            for i in range(n+1-l):
                if math.gcd(*nums[i:i+l]) == 1:
                    return l-1 + n-1
        return -1