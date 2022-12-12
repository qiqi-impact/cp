class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        f = defaultdict(int)
        f[0] = 1
        p = 0
        ret = 0
        for n in nums:
            p += n
            p %= k
            ret += f[p]
            f[p] += 1
        return ret