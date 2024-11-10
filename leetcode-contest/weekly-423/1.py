class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def isinc(x):
            for i in range(len(x) - 1):
                if x[i+1] <= x[i]:
                    return False
            return True
        
        for i in range(len(nums) - 2 * k + 1):
            a, b = nums[i:i+k], nums[i+k:i+2*k]
            if isinc(a) and isinc(b):
                return True
        return False