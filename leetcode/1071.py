def div(a, b):
    s = ''
    while len(s) < len(b):
        s += a
        if s == b:
            return True
    return False

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        mn = min(len(str1), len(str2))
        for l in range(mn, 0, -1):
            if div(str1[:l], str1) and div(str1[:l], str2):
                return str1[:l]
        return ''