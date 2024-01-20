class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 1
        
        ct = Counter(nums)
        x = nums[0]
        mn = nums[0]
        for i in range(1, len(nums)):
            x = math.gcd(x, nums[i])
            mn = min(mn, nums[i])
            
        if x < mn:
            return 1
        
        return max(1, (ct[mn]+1)//2)