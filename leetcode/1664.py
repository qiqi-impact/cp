class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        sf = [[0,0] for _ in range(n+1)]
        for i in range(len(nums)-1, -1, -1):
            sf[i] = sf[i+1][:]
            sf[i][i%2] = sf[i+1][i%2] + nums[i]
        ret = 0
        cur = [0,0]
        for i in range(len(nums)):
            if sf[i+1][0] + cur[1] == sf[i+1][1] + cur[0]:
                ret += 1
            cur[i%2] += nums[i]
        return ret