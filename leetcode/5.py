class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ret = 0
        idx = 0
        for i in range(n):
            a, b = i, i
            while a >= 0 and b < n and s[a] == s[b]:
                l = b - a + 1
                if l > ret:
                    ret = l
                    idx = a
                a -= 1
                b += 1
            a, b = i, i+1
            while a >= 0 and b < n and s[a] == s[b]:
                l = b - a + 1
                if l > ret:
                    ret = l
                    idx = a
                a -= 1
                b += 1
        return s[idx:idx+ret]