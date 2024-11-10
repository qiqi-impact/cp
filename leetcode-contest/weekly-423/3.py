class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9+7
        ret = 0
        d = defaultdict(int)
        sm = defaultdict(int)
        for x in nums:
            v = d[x-1] + d[x+1] + 1
            s = sm[x-1] + sm[x+1] + v * x
            ret += s
            ret %= MOD
            d[x] += v
            d[x] %= MOD
            sm[x] += s
            sm[x] %= MOD
        return ret
            