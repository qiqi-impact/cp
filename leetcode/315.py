class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        l = []
        ret = [None] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            idx = bisect_left(l, nums[i])
            ret[i] = idx
            l.insert(idx, nums[i])
        return ret