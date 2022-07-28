class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        
        @cache
        def dfs(idx, assigned):
            if idx == len(nums):
                return 0
            ret = 0
            cur = assigned
            for i in range(numSlots):
                if cur % 3 < 2:
                    ret = max(ret, (nums[idx] & (i+1)) + dfs(idx+1, assigned + pow(3, i)))
                cur //= 3
            return ret
        
        return dfs(0, 0)