class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s)+1)
        dp[0] = 1
        for i in range(len(s)):
            x = int(s[i])
            if 1 <= x <= 26:
                dp[i+1] += dp[i]
            if i > 0 and s[i-1] != '0':
                x += int(s[i-1]) * 10
                if 1 <= x <= 26:
                    dp[i+1] += dp[i-1]
        return dp[-1]