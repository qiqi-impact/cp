class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n = len(nums)
        @cache
        def dp(idx, left1, left2):
            if idx == n:
                return 0
            ret = nums[idx] + dp(idx+1, left1, left2)
            if left1 and left2:
                if nums[idx] >= k:
                    ret = min(ret, (nums[idx] - k + 1)//2 + dp(idx+1, left1-1, left2-1))
                if (nums[idx] + 1) // 2 >= k:
                    ret = min(ret, (nums[idx] + 1)//2 - k + dp(idx+1, left1-1, left2-1))
            if left1:
                ret = min(ret, (nums[idx] + 1)//2 + dp(idx+1, left1-1, left2))
            if left2 and nums[idx] >= k:
                ret = min(ret, nums[idx] - k + dp(idx+1, left1, left2-1))
            return ret
        return dp(0, op1, op2)