class Solution:
    def processStr(self, s: str) -> str:
        l = []
        for c in s:
            if c == '*':
                if l:
                    l.pop()
            elif c == '#':
                l += l
            elif c == '%':
                l = l[::-1]
            else:
                l.append(c)
        return ''.join(l)©leetcode