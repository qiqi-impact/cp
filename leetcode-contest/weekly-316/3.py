class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        l = sorted(list(zip(nums, cost)))
        n = len(nums)
        a = [0] * n
        b = [0] * n
        cur = l[0][1]
        for i in range(1, n):
            a[i] = a[i-1] + cur * (l[i][0] - l[i-1][0])
            cur += l[i][1]
        mn = float('inf')
        cur = l[-1][1]
        for i in range(n-2, -1, -1):
            b[i] = b[i+1] + cur * (l[i+1][0] - l[i][0])
            cur += l[i][1]
        for i in range(n):
            mn = min(mn, a[i] + b[i])
        return mn