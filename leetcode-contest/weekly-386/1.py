class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        ct = Counter(nums)
        for v in ct.values():
            if v >= 3:
                return False
        return True