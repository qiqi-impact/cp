class Solution:
    def squareIsWhite(self, c: str) -> bool:
        x = int(c[1])
        y = ord(c[0]) - 97
        return not (x+y)%2