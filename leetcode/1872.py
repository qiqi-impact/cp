class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        pf = [0]
        for x in stones:
            pf.append(pf[-1] + x)
        
        dp = [-inf] * (n+1)
        dp[n] = 0
        
        mx = pf[n]
        for i in range(n-1, 1, -1):
            dp[i] = mx
            mx = max(mx, pf[i]-dp[i])
        return mx