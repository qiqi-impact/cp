class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s = [ord(c)-ord('A') for c in s]
        j = 0
        f = [0] * 26
        ret = k
        for i in range(len(s)):
            while j < len(s):
                f[s[j]] += 1
                if (j - i + 1) - max(f) > k:
                    f[s[j]] -= 1
                    break
                ret = max(ret, j - i + 1)
                j += 1
            f[s[i]] -= 1
        return ret