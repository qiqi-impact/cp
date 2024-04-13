class Solution:
    def scoreOfString(self, s: str) -> int:
        l = [ord(c)-97 for c in s]
        ret = 0
        for i in range(1, len(l)):
            ret += abs(l[i] - l[i-1])
        return ret