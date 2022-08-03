class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        ri = 0
        ret = 0
        for i in range(len(nums)):
            if nums[ri] <= nums[i]:
                ri = i
        ret += len(nums) - 1 - ri
        li = 0
        for i in range(len(nums)):
            if nums[li] > nums[i]:
                li = i
        ret += li
        if li > ri:
            ret -= 1
        return ret