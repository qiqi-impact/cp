class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        ls = [0] * (n+1)
        for x, y in queries:
            ls[x] += 1
            ls[y+1] -= 1
        cur = 0
        for i in range(n):
            cur += ls[i]
            if cur < nums[i]:
                return False
        return True