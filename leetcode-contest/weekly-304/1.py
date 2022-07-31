class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set(nums)
        s.discard(0)
        return len(s)