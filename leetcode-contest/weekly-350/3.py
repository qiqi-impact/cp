class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        @cache
        def dfs(idx, used, lst):
            if idx == len(nums):
                return 1
            ret = 0
            for i in range(len(nums)):
                if (1 << i) & used == 0:
                    if (idx == 0) or (nums[i] % nums[lst] == 0) or (nums[lst] % nums[i] == 0):
                        ret += dfs(idx+1, used ^ (1 << i), i)
            return ret % (10**9+7)
        return dfs(0,0,None)