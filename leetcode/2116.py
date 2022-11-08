class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2 != 0: return False
        ct = 0
        for i in range(len(s)):
            if locked[i] == '0' or s[i] == '(':
                ct += 1
            else:
                ct -= 1
                if ct < 0:
                    return False
        ct = 0
        for i in range(len(s)-1, -1, -1):
            if locked[i] == '0' or s[i] == ')':
                ct += 1
            else:
                ct -= 1
                if ct < 0:
                    return False
        return True