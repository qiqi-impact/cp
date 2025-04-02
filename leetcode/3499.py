class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ret = s.count('1')
        add = 0
        l = [int(x) for x in s]
        l = [(1, 1)] + ([(k, len(list(g))) for k, g in groupby(l)]) + [(1, 1)]
        for i in range(1, len(l)-1):
            if l[i][0] == 1 and l[i-1][0] == 0 and l[i+1][0] == 0:
                add = max(add, l[i-1][1] + l[i+1][1])
        return ret + add