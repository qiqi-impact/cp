class Solution:
    def processStr(self, s: str, k: int) -> str:
        l = []
        cl = 0
        for c in s:
            if c == '#':
                cl *= 2
            elif c == '%':
                pass
            elif c == '*':
                cl = max(0, cl - 1)
            else:
                cl += 1
            l.append(cl)
        for i in range(len(l)-1, -1, -1):
            if s[i] == '*':
                if k >= l[i]:
                    return '.'
            elif s[i] == '%':
                k = l[i] - 1 - k
            elif s[i] == '#':
                if k >= l[i] // 2:
                    k -= l[i] // 2
            else:
                if l[i] == k + 1:
                    return s[i]
        return '.'
                ©leetcode