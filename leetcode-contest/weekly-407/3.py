class Solution:
    def maxOperations(self, s: str) -> int:
        l = []
        s += '1'
        for i in range(len(s)):
            if s[i] == '1':
                l.append(i)
        r = []
        for i in range(len(l) - 1):
            r.append(l[i+1] - l[i])
        ct = 0
        op = 0
        for x in r:
            ct += 1
            if x != 1:
                op += ct
        return op