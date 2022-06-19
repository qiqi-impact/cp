class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ret = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                ret += 1
            elif k >= 1:
                k -= 1
                ret += 1
            k //= 2
        return ret