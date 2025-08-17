class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9+7
        n = len(nums)
        m = [1] * n
        for l, r, k, v in queries:
            for i in range(l, r + 1, k):
                m[i] *= v
                m[i] %= MOD
        cur = 0
        for i, x in enumerate(nums):
            cur ^= (x * m[i]) % MOD
        return cur