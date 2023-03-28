class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        d = defaultdict(int)
        ret = 0
        d[0] = 1
        cur = 0
        for x in nums:
            cur ^= x
            ret += d[cur]
            d[cur] += 1
        return ret