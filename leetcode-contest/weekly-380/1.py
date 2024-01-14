class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ct = Counter(nums)
        mx = max(ct.values())
        ret = 0
        for k in ct:
            if ct[k] == mx:
                ret += mx
        return ret