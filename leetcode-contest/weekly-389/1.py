class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rs = s[::-1]
        for i in range(len(s)-1):
            x = s[i:i+2]
            if x in rs:
                return True
        return False