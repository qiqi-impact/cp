class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = (0, -1)
        for i in range(len(s)):
            for j in range(len(s)):
                if 0 <= i-j and i+j < len(s):
                    if s[i-j] != s[i+j]:
                        break
                    else:
                        if ret[1] - ret[0] + 1 < 2*j+1:
                            ret = (i-j, i+j)
                else:
                    break
            for j in range(len(s)):
                if 0 <= i-j and i+j+1 < len(s):
                    if s[i-j] != s[i+j+1]:
                        break
                    else:
                        if ret[1] - ret[0] + 1 < 2*j+2:
                            ret = (i-j, i+j+1)
                else:
                    break
        return s[ret[0]:ret[1]+1]