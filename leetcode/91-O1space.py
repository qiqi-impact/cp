class Solution:
    def numDecodings(self, s: str) -> int:
        a, b = 0, 1
        for i in range(len(s)):
            x = int(s[i])
            c = 0
            if 1 <= x <= 26:
                c += b
            if i > 0 and s[i-1] != '0':
                x += int(s[i-1]) * 10
                if 1 <= x <= 26:
                    c += a
            a, b = b, c
        return b