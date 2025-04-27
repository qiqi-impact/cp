class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        sn = [str(x) for x in nums]
        n = len(nums)
        @cache
        def dp(bm, sofar):
            if bm == 0:
                return (False, []) if sofar else (True, [])
            for i in range(n):
                if bm & 1 << i:
                    ns = (sofar * (10 ** len(sn[i])) + nums[i]) % k
                    a, b = dp(bm ^ 1 << i, ns)
                    if a:
                        return (True, [nums[i]] + b[:])
            return (False, [])
        return dp((1 << n) - 1, 0)[1]