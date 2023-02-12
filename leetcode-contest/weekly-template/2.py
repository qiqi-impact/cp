class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ret = 0
        for x in nums:
            l = bisect.bisect_left(nums, lower - x)
            r = bisect.bisect(nums, upper - x)
            ret += r - l
            if lower <= 2 * x <= upper: # remove overcount if i == j satisfies lower <= nums[i] + nums[j] <= upper
                ret -= 1
        return ret // 2 # every pair will be counted twice as (i, j) or (j, i)