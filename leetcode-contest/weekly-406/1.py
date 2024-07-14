class Solution:
    def getSmallestString(self, s: str) -> str:
        l = [c for c in s]
        for i in range(len(s)-1):
            if (int(s[i]) - int(s[i+1])) % 2 == 0 and int(s[i]) > int(s[i+1]):
                return s[:i] + s[i+1] + s[i] + s[i+2:]
        return s