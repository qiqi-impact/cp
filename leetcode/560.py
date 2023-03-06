class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        cur = 0
        ret = 0
        for x in nums:
            cur += x
            ret += freq[cur - k]
            freq[cur] += 1
        return ret