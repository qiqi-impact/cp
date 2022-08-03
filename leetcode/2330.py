class Solution:
    def makePalindrome(self, s: str) -> bool:
        ret = 0
        for i in range(len(s)//2):
            if s[i] != s[len(s)-1-i]:
                ret += 1
                if ret == 3:
                    return False
        return True