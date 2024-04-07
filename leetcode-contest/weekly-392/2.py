class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def dst(x, y):
            xx, yy = ord(x), ord(y)
            xx, yy = max(xx, yy), min(xx, yy)
            return min(xx - yy, yy + 26 - xx)
        ret = ''
        for i in range(len(s)):
            for x in string.ascii_lowercase:
                v = dst(x, s[i])
                if v <= k:
                    k -= v
                    ret += x
                    break
        return ret
                    