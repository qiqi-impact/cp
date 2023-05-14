class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)//2
        FULL = 2 ** (2 * n) - 1
        
        @cache
        def dp(mask):
            if mask == FULL:
                return 0

            score = bin(mask).count('1')//2 + 1

            ret = -inf
            for i in range(2*n):
                if not (mask & (1 << i)):
                    for j in range(i+1, 2*n):
                        if not (mask & (1 << j)):
                            nm = mask ^ (1 << i) ^ (1 << j)
                            ret = max(ret, dp(nm) + score * gcd(nums[i], nums[j]))
            return ret

        return dp(0)