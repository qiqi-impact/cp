class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ct = defaultdict(int)
        ct[0] = 1
        ret = 0
        cur = 0
        for x in nums:
            cur += x%2
            ret += ct[cur - k]
            ct[cur] += 1
        return ret