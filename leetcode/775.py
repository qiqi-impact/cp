class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        d = {}
        for i in range(len(nums)):
            if i != nums[i]:
                d[i] = nums[i]
        for k in d:
            v = d[k]
            if abs(k - v) > 1:
                return False
            if d.get(v, None) != k:
                return False
        return True