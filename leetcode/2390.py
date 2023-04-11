class Solution:
    def removeStars(self, s: str) -> str:
        ret = []
        for c in s:
            if c == '*':
                if ret:
                    ret.pop()
            else:
                ret.append(c)
        return ''.join(ret)