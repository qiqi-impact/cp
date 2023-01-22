class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        @cache
        def dp(i):
            if i == len(nums):
                return 0
            ret = inf
            d = defaultdict(int)
            sm = k
            for j in range(i, len(nums)):
                d[nums[j]] += 1
                if d[nums[j]] == 2:
                    sm += 2
                elif d[nums[j]] > 2:
                    sm += 1
                ret = min(ret, sm + dp(j+1))
            return ret
        return dp(0)