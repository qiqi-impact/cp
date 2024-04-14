class Solution:
    def minimumValueSum(self, nums: List[int], av: List[int]) -> int:
        n, m = len(nums), len(av)
        
        @cache
        def dp(i, j, cur):
            if i == n:
                return 0 if j == m else inf
            if j == m:
                return inf
            if cur == -1:
                cur = nums[i]
            nx = cur & nums[i]
            ret = dp(i+1, j, nx)
            if nx == av[j]:
                ret = min(ret, nums[i] + dp(i+1, j+1, -1))
            return ret
        
        q = dp(0, 0, -1)
        return q if q != inf else -1