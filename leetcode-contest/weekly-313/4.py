class Solution:
    def deleteString(self, s: str) -> int:
        dp = [1] * (len(s))
        for i in range(len(s)-1, -1, -1):
            for j in range(1, len(s)):
                if i+2*j > len(s):
                    break
                if 1 + dp[i+j] > dp[i] and s[i:i+j] == s[i+j:i+2*j]:
                    dp[i] = 1 + dp[i+j]
        return dp[0]