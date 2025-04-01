@cache
def ispal(x):
    for i in range(len(x)//2):
        if x[i] != x[-i-1]:
            return False
    return True

class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        ret = 1
        for i in range(len(s)+1):
            for j in range(i, len(s)+1):
                for k in range(len(t)+1):
                    for l in range(k, len(t)+1):
                        if ispal(s[i:j]+t[k:l]):
                            ret = max(ret, j - i + l - k)
        return ret