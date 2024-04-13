class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        n = len(nums)
        @cache
        def f(idx, x):
            if idx == -1:
                return int(x == 0)
            r = 2 * f(idx-1, x)
            if x >= nums[idx]:
                r += f(idx - 1, x - nums[idx])
            return r % (10**9+7)
        return f(n-1, k)