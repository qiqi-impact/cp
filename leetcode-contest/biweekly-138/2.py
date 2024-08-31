class Solution:
    def stringHash(self, s: str, k: int) -> str:
        ret = ''
        n = len(s)
        for i in range(n//k):
            t = 0
            for j in range(k):
                t += int(ord(s[i*k+j])-97)
            t %= 26
            ret += chr(97+t)
        return ret