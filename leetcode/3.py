class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        d = defaultdict(int)
        ret = 0
        for i in range(len(s)):
            if i > 0:
                d[s[i-1]] -= 1
            while j < len(s) and d[s[j]] == 0:
                d[s[j]] = 1
                j += 1
            ret = max(ret, j - i)
        return ret