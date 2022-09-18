class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        s = [ord(x) for x in s]
        cur = s[0]
        ln = 1
        mx = 1
        for i in range(1, len(s)):
            c = s[i]
            if c == cur + 1:
                cur = c
                ln += 1
                mx = max(mx, ln)
            else:
                ln = 1
                cur = c
        return mx
                