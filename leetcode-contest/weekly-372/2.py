class Solution:
    def minimumSteps(self, s: str) -> int:
        ret = 0
        ct = 0
        for i in range(len(s)):
            if s[i] == '0':
                ret += i - ct
                ct += 1
        return ret