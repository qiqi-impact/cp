class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        d = [-inf] * (target+1)
        d[0] = 0
        for x in nums:
            for i in range(target, x-1, -1):
                d[i] = max(d[i], d[i-x] + 1)
        return max(-1, d[target])