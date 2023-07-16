class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        ct = Counter(nums)
        dom = None
        for k in ct:
            if ct[k] * 2 > n:
                dom = k
                break
        tot = 0
        for i in range(n-1):
            if nums[i] == dom:
                tot += 1
            a, b = tot, i+1
            c, d = ct[dom] - tot, n - (i+1)
            if a * 2 > b and c * 2 > d:
                return i
        return -1