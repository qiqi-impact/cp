class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(x):
            return int(str(x)[::-1])
        d = defaultdict(int)
        l = [x - rev(x) for x in nums]
        for x in l:
            d[x] += 1
        MOD = int(1e9)+7
        ret = 0
        for k in d:
            ret += d[k] * (d[k]-1) // 2
            ret %= MOD
        return ret