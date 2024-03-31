class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        ret = 0
        cur = 0
        lst = nums[0]
        for x in nums:
            if x != lst:
                cur += 1
            else:
                cur = 1
            ret += cur
            lst = x
        return ret