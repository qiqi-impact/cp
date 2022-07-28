class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dp(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if word1[i] == word2[j]:
                return dp(i+1, j+1)
            return 1 + min(dp(i+1, j), dp(i, j+1))
        return dp(0, 0)