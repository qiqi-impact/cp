class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        d = {}
        seen = set()
        for i, x in enumerate(nums):
            for y in seen:
                df = x - y
                d[x, df] = max(d.get((x, df), 0), d.get((y, df), 1) + 1)
            seen.add(x)
        return max(d.values())