class Solution:
    def solve(self, s):
        if len(s) < 2: return 0
        @cache
        def ls(i, j):
            if i == len(s) or j == len(s) or s[i] != s[j]:
                return 0
            return 1 + ls(i+1, j+1)
        ret = 0
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                ret = max(ret, ls(i, j))
        return ret