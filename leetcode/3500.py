class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        n = len(nums)

        pfn = [0]
        for x in nums:
            pfn.append(pfn[-1] + x)

        pfc = [0]
        for x in cost:
            pfc.append(pfc[-1] + x)
        
        @cache
        def dp(idx):
            if idx == n:
                return 0
            mn = inf
            for i in range(idx+1, n+1):
                left = pfn[i] + k
                right = pfc[i] - pfc[idx]
                cur = left * right + dp(i) + k * (pfc[n] - pfc[i])
                mn = min(mn, cur)
            return mn

        return dp(0)w
