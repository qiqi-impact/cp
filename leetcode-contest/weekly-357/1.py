class Solution:
    def finalString(self, s: str) -> str:
        ret = ''
        for c in s:
            if c == 'i':
                ret = ret[::-1]
            else:
                ret += c
        return ret