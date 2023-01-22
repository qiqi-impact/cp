class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        a = s.count('1') == 0
        b = target.count('1') == 0
        return a == b
        