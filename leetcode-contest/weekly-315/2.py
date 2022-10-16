class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        l = [str(x) for x in nums]
        l += [x[::-1] for x in l]
        l = [int(x) for x in l]
        return len(set(l))