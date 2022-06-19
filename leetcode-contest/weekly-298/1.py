class Solution:
    def greatestLetter(self, s: str) -> str:
        for i in range(25, -1, -1):
            c = chr(ord('a') + i)
            if c in s and c.upper() in s:
                return c.upper()
        return ''