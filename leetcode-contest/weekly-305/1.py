class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = set(nums)
        ret = 0
        for n in nums:
            if n+diff in s and n-diff in s:
                ret += 1
        return ret