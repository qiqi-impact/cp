class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        MOD = 10**9+7
        sm = 0
        ret = 0
        nums.sort()
        for i, x in enumerate(nums):
            sm = 2 * sm + x
            if i > 0:
                sm -= nums[i-1]
                sm %= MOD
            ret += x * x * sm
            ret %= MOD
        return ret