class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        a = [ord(c)-97 for c in str1]
        b = [ord(c)-97 for c in str2]
        bp = 0
        for x in a:
            if b[bp] == x or b[bp] == (x+1)%26:
                bp += 1
                if bp == len(b):
                    return True
        return False