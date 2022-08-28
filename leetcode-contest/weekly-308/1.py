class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        nums = [0] + nums
        ret = []
        for q in queries:
            v = bisect_right(nums, q) - 1
            ret.append(v)
        return ret