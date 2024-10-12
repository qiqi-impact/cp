class Solution:
    def maxRemovals(self, s: str, p: str, t: List[int]) -> int:
        t = set(t)
        dp = [[-inf for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        for j in range(len(p)+1):
            dp[len(s)][j] = -inf if j != len(p) else 0
        for i in range(len(s)-1, -1, -1):
            dp[i][len(p)] = int(i in t) + dp[i+1][len(p)]
        for i in range(len(s)-1, -1, -1):
            for j in range(len(p)-1, -1, -1):
                dp[i][j] = int(i in t) + dp[i+1][j]
                if s[i] == p[j]:
                    dp[i][j] = max(dp[i][j], dp[i+1][j+1])
        return dp[0][0]
