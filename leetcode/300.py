class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = []
        for n in nums:
            idx = bisect.bisect_left(l, n)
            if idx == len(l):
                l.append(n)
            else:
                l[idx] = n
        return len(l)