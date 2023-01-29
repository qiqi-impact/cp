class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        lt = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            sm = 0
            for j in range(n):
                if nums[j] <= i+1:
                    sm += 1
                lt[i][j] = sm
        ret = 0
        for i in range(1, n-1):
            for j in range(i+1, n-1):
                if nums[i] > nums[j]:
                    v = lt[nums[j]-1][i-1] * (n - nums[i] - (j + 1 - lt[nums[i]-1][j]))
                    ret += v
        return ret