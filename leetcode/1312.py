class Solution:
    def minInsertions(self, s: str) -> int:
        @cache
        def dp(i, j):
            if i >= j:
                return 0
            if s[i] == s[j]:
                return dp(i+1, j-1)
            return 1+min(dp(i+1, j), dp(i,j-1))
        return dp(0, len(s)-1)