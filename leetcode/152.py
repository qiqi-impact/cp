class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mn = mx = ans = nums[0]
        for i in range(1, len(nums)):
            q = (nums[i], nums[i]*mx, nums[i]*mn)
            mn, mx = min(*q), max(*q)
            ans = max(ans, mx)
        return ans
                