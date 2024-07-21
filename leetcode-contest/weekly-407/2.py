class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for x in 'aeiou':
            if x in s:
                return True
        return False