class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        p = [0]
        for x in nums:
            p.append(p[-1] + x)
        ret = []
        for q in queries:
            idx = bisect.bisect_left(nums, q)
            ret.append(idx * q - p[idx] + (p[-1] - p[idx]) - (len(p) - 1 - idx) * q)
        return ret