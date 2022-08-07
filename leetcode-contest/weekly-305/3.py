class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        @cache
        def dfs(idx):
            if idx == n:
                return True
            if n - idx >= 2 and nums[idx] == nums[idx+1]:
                if dfs(idx+2):
                    return True
            if n - idx >= 3 and (nums[idx] == nums[idx+1] == nums[idx+2] or nums[idx+1] - nums[idx] == nums[idx+2] - nums[idx+1] == 1):
                if dfs(idx+3):
                    return True
            return False
        return dfs(0)