class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        s = [ord(c)-97 for c in s]
        l = [0] * 26
        for x in s:
            mx = 0
            for i in range(26):
                if abs(x - i) <= k:
                    mx = max(mx, 1 + l[i])
            l[x] = mx
        return max(l)