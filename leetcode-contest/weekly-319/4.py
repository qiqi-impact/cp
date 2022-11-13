class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        dp = [0] * (len(s)+1)
        for i in range(len(s)):
            if i > 0:
                dp[i] = max(dp[i], dp[i-1])
            for j in range(len(s)):
                a, b = i-j, i+j
                if a < 0 or b >= len(s): break
                if s[a] == s[b]:
                    if b - a + 1 >= k:
                        dp[b+1] = max(dp[b+1], 1 + dp[a])
                        break
                else:
                    break
            for j in range(len(s)-1):
                a, b = i-j, i+j+1
                if a < 0 or b >= len(s): break
                if s[a] == s[b]:
                    if b - a + 1 >= k:
                        dp[b+1] = max(dp[b+1], 1 + dp[a])
                        break
                else:
                    break
        return max(dp)