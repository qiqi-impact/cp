class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        l = [ord(c)-97 for c in s]
        dp = [0 for _ in range(26)]
        dp[l[0]] = 1
        for i in range(1, len(l)):
            m = 1
            for j in range(l[i]-k, l[i]+k+1):
                if 0 <= j < 26:
                    m = max(m, 1 + dp[j])
            dp[l[i]] = m
        return max(dp)