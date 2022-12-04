class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        sm = 0
        for i in range(n):
            sm += nums[i]
            left[i] = sm
        sm = 0
        for i in range(n-1, -1, -1):
            sm += nums[i]
            right[i] = sm
        idx = -1
        v = inf
        for i in range(n):
            q = right[i+1]//(n-i-1) if i < (n-1) else 0
            cur = abs(left[i]//(i+1) - q)
            if cur < v:
                v = cur
                idx = i
        return idx